# Python decorators

This is a project designed to provide a series of python decorators that can be useful in diagnosing and developing your projects.

## List of decorators currently available

1. **Time Counter**

   Decorator for functions that calculate execution time.

2. **Log**

   Returns the inputs and output of the function.

3. **Disk Cache**

   Stores the result of running the function for future use if necessary.

4. **Rate Limit**

   Limits the number of calls to a function within a time period.

5. **Exponential Backoff**

   Technique used to prevent a system from being overwhelmed with requests.

6. **Memoize**

   Caches function results in memory for faster subsequent calls. Perfect for expensive computations and recursive functions like Fibonacci.

7. **Retry**

   Automatically retries a function a specified number of times on failure. Useful for network requests and unreliable operations.

8. **Deprecated**

   Marks functions as deprecated and issues warnings when called. Helps maintain backward compatibility while encouraging migration to newer alternatives.

9. **Validate**

   Validates function arguments against custom conditions before execution. Useful for input validation and enforcing constraints.
