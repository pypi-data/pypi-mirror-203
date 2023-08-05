// Copyright 2007, Google Inc.
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
//     * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above
// copyright notice, this list of conditions and the following disclaimer
// in the documentation and/or other materials provided with the
// distribution.
//     * Neither the name of Google Inc. nor the names of its
// contributors may be used to endorse or promote products derived from
// this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
// Author: wan@google.com (Zhanyong Wan)

// Tests that Google Mock constructs can be used in a large number of
// threads concurrently.

#include "gmock/gmock.h"

#include "gtest/gtest.h"

namespace testing {
namespace {

// From "gtest/internal/gtest-port.h".
using ::testing::internal::ThreadWithParam;

// The maximum number of test threads (not including helper threads)
// to create.
const int kMaxTestThreads = 50;

// How many times to repeat a task in a test thread.
const int kRepeat = 50;

class MockFoo {
 public:
  MOCK_METHOD1(Bar, int(int n));  // NOLINT
  MOCK_METHOD2(Baz, char(const char* s1, const std::string& s2));  // NOLINT
};

// Helper for waiting for the given thread to finish and then deleting it.
template <typename T>
void JoinAndDelete(ThreadWithParam<T>* t) {
  t->Join();
  delete t;
}

using internal::linked_ptr;

// Helper classes for testing using linked_ptr concurrently.

class Base {
 public:
  explicit Base(int a_x) : x_(a_x) {}
  virtual ~Base() {}
  int x() const { return x_; }
 private:
  int x_;
};

class Derived1 : public Base {
 public:
  Derived1(int a_x, int a_y) : Base(a_x), y_(a_y) {}
  int y() const { return y_; }
 private:
  int y_;
};

class Derived2 : public Base {
 public:
  Derived2(int a_x, int a_z) : Base(a_x), z_(a_z) {}
  int z() const { return z_; }
 private:
  int z_;
};

linked_ptr<Derived1> pointer1(new Derived1(1, 2));
linked_ptr<Derived2> pointer2(new Derived2(3, 4));

struct Dummy {};

// Tests that we can copy from a linked_ptr and read it concurrently.
void TestConcurrentCopyAndReadLinkedPtr(Dummy /* dummy */) {
  // Reads pointer1 and pointer2 while they are being copied from in
  // another thread.
  EXPECT_EQ(1, pointer1->x());
  EXPECT_EQ(2, pointer1->y());
  EXPECT_EQ(3, pointer2->x());
  EXPECT_EQ(4, pointer2->z());

  // Copies from pointer1.
  linked_ptr<Derived1> p1(pointer1);
  EXPECT_EQ(1, p1->x());
  EXPECT_EQ(2, p1->y());

  // Assigns from pointer2 where the LHS was empty.
  linked_ptr<Base> p2;
  p2 = pointer1;
  EXPECT_EQ(1, p2->x());

  // Assigns from pointer2 where the LHS was not empty.
  p2 = pointer2;
  EXPECT_EQ(3, p2->x());
}

const linked_ptr<Derived1> p0(new Derived1(1, 2));

// Tests that we can concurrently modify two linked_ptrs that point to
// the same object.
void TestConcurrentWriteToEqualLinkedPtr(Dummy /* dummy */) {
  // p1 and p2 point to the same, shared thing.  One thread resets p1.
  // Another thread assigns to p2.  This will cause the same
  // underlying "ring" to be updated concurrently.
  linked_ptr<Derived1> p1(p0);
  linked_ptr<Derived1> p2(p0);

  EXPECT_EQ(1, p1->x());
  EXPECT_EQ(2, p1->y());

  EXPECT_EQ(1, p2->x());
  EXPECT_EQ(2, p2->y());

  p1.reset();
  p2 = p0;

  EXPECT_EQ(1, p2->x());
  EXPECT_EQ(2, p2->y());
}

// Tests that different mock objects can be used in their respective
// threads.  This should generate no Google Test failure.
void TestConcurrentMockObjects(Dummy /* dummy */) {
  // Creates a mock and does some typical operations on it.
  MockFoo foo;
  ON_CALL(foo, Bar(_))
      .WillByDefault(Return(1));
  ON_CALL(foo, Baz(_, _))
      .WillByDefault(Return('b'));
  ON_CALL(foo, Baz(_, "you"))
      .WillByDefault(Return('a'));

  EXPECT_CALL(foo, Bar(0))
      .Times(AtMost(3));
  EXPECT_CALL(foo, Baz(_, _));
  EXPECT_CALL(foo, Baz("hi", "you"))
      .WillOnce(Return('z'))
      .WillRepeatedly(DoDefault());

  EXPECT_EQ(1, foo.Bar(0));
  EXPECT_EQ(1, foo.Bar(0));
  EXPECT_EQ('z', foo.Baz("hi", "you"));
  EXPECT_EQ('a', foo.Baz("hi", "you"));
  EXPECT_EQ('b', foo.Baz("hi", "me"));
}

// Tests invoking methods of the same mock object in multiple threads.

struct Helper1Param {
  MockFoo* mock_foo;
  int* count;
};

void Helper1(Helper1Param param) {
  for (int i = 0; i < kRepeat; i++) {
    const char ch = param.mock_foo->Baz("a", "b");
    if (ch == 'a') {
      // It was an expected call.
      (*param.count)++;
    } else {
      // It was an excessive call.
      EXPECT_EQ('\0', ch);
    }

    // An unexpected call.
    EXPECT_EQ('\0', param.mock_foo->Baz("x", "y")) << "Expected failure.";

    // An uninteresting call.
    EXPECT_EQ(1, param.mock_foo->Bar(5));
  }
}

// This should generate 3*kRepeat + 1 failures in total.
void TestConcurrentCallsOnSameObject(Dummy /* dummy */) {
  MockFoo foo;

  ON_CALL(foo, Bar(_))
      .WillByDefault(Return(1));
  EXPECT_CALL(foo, Baz(_, "b"))
      .Times(kRepeat)
      .WillRepeatedly(Return('a'));
  EXPECT_CALL(foo, Baz(_, "c"));  // Expected to be unsatisfied.

  // This chunk of code should generate kRepeat failures about
  // excessive calls, and 2*kRepeat failures about unexpected calls.
  int count1 = 0;
  const Helper1Param param = { &foo, &count1 };
  ThreadWithParam<Helper1Param>* const t =
      new ThreadWithParam<Helper1Param>(Helper1, param, NULL);

  int count2 = 0;
  const Helper1Param param2 = { &foo, &count2 };
  Helper1(param2);
  JoinAndDelete(t);

  EXPECT_EQ(kRepeat, count1 + count2);

  // foo's destructor should generate one failure about unsatisfied
  // expectation.
}

// Tests using the same mock object in multiple threads when the
// expectations are partially ordered.

void Helper2(MockFoo* foo) {
  for (int i = 0; i < kRepeat; i++) {
    foo->Bar(2);
    foo->Bar(3);
  }
}

// This should generate no Google Test failures.
void TestPartiallyOrderedExpectationsWithThreads(Dummy /* dummy */) {
  MockFoo foo;
  Sequence s1, s2;

  {
    InSequence dummy;
    EXPECT_CALL(foo, Bar(0));
    EXPECT_CALL(foo, Bar(1))
        .InSequence(s1, s2);
  }

  EXPECT_CALL(foo, Bar(2))
      .Times(2*kRepeat)
      .InSequence(s1)
      .RetiresOnSaturation();
  EXPECT_CALL(foo, Bar(3))
      .Times(2*kRepeat)
      .InSequence(s2);

  {
    InSequence dummy;
    EXPECT_CALL(foo, Bar(2))
        .InSequence(s1, s2);
    EXPECT_CALL(foo, Bar(4));
  }

  foo.Bar(0);
  foo.Bar(1);

  ThreadWithParam<MockFoo*>* const t =
      new ThreadWithParam<MockFoo*>(Helper2, &foo, NULL);
  Helper2(&foo);
  JoinAndDelete(t);

  foo.Bar(2);
  foo.Bar(4);
}

// Tests using Google Mock constructs in many threads concurrently.
TEST(StressTest, CanUseGMockWithThreads) {
  void (*test_routines[])(Dummy dummy) = {
    &TestConcurrentCopyAndReadLinkedPtr,
    &TestConcurrentWriteToEqualLinkedPtr,
    &TestConcurrentMockObjects,
    &TestConcurrentCallsOnSameObject,
    &TestPartiallyOrderedExpectationsWithThreads,
  };

  const int kRoutines = sizeof(test_routines)/sizeof(test_routines[0]);
  const int kCopiesOfEachRoutine = kMaxTestThreads / kRoutines;
  const int kTestThreads = kCopiesOfEachRoutine * kRoutines;
  ThreadWithParam<Dummy>* threads[kTestThreads] = {};
  for (int i = 0; i < kTestThreads; i++) {
    // Creates a thread to run the test function.
    threads[i] =
        new ThreadWithParam<Dummy>(test_routines[i % kRoutines], Dummy(), NULL);
    GTEST_LOG_(INFO) << "Thread #" << i << " running . . .";
  }

  // At this point, we have many threads running.
  for (int i = 0; i < kTestThreads; i++) {
    JoinAndDelete(threads[i]);
  }

  // Ensures that the correct number of failures have been reported.
  const TestInfo* const info = UnitTest::GetInstance()->current_test_info();
  const TestResult& result = *info->result();
  const int kExpectedFailures = (3*kRepeat + 1)*kCopiesOfEachRoutine;
  GTEST_CHECK_(kExpectedFailures == result.total_part_count())
      << "Expected " << kExpectedFailures << " failures, but got "
      << result.total_part_count();
}

}  // namespace
}  // namespace testing

int main(int argc, char **argv) {
  testing::InitGoogleMock(&argc, argv);

  const int exit_code = RUN_ALL_TESTS();  // Expected to fail.
  GTEST_CHECK_(exit_code != 0) << "RUN_ALL_TESTS() did not fail as expected";

  printf("\nPASS\n");
  return 0;
}
