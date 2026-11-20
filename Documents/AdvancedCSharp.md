## Advanced C# Concepts a Senior Developer Should Use Daily

1. **Generics** — Write type-safe, reusable code without duplicating logic for each type (`List<T>`, `Repository<T>`).
2. **Reflection** — Inspect and invoke types, methods, and properties at runtime via `System.Reflection`.
3. **Dependency Injection** — Decouple components by injecting dependencies rather than constructing them inside a class.
4. **Interfaces** — Define contracts that multiple types can implement, enabling polymorphism and testability.
5. **Implicit and Explicit Operators** — Define custom type conversions: `implicit` (automatic) and `explicit` (requires a cast).
6. **Smart Constructors** — Use factory methods or private constructors to ensure objects are always created in a valid state.
7. **Extension Methods** — Add methods to existing types without modifying them; group utilities in static classes.
8. **Import Static Members** — Use `using static` to call static members without the class prefix, reducing verbosity.
9. **Global Usings** — Declare `using` statements once in a central file to apply them project-wide.
10. **Clean Code Principles** — Meaningful names, small focused functions, single responsibility, no magic numbers.
11. **Avoid Primitive Obsession** — Wrap raw types (`string`, `int`) in value objects to give them domain meaning and built-in validation.
12. **Validation** — Validate inputs at system boundaries using FluentValidation, Data Annotations, or guard clauses.
13. **Regex** — Use `System.Text.RegularExpressions` for pattern matching; prefer source-generated regexes for performance.
14. **Value Objects** — Immutable types defined by their value, not identity (e.g. `Money`, `Email`, `Address`).
15. **Indexers** — Allow class instances to be accessed with array-like syntax using `this[int index]`.
16. **Operator Overloading** — Define custom behaviour for operators (`+`, `-`, `==`) on your own types.
17. **Factories** — Encapsulate object creation logic in factory methods or classes to keep constructors simple.
18. **LINQ** — Query collections with composable operators: `Where`, `Select`, `GroupBy`, `FirstOrDefault`, `Aggregate`.
19. **Design Patterns** — Apply proven solutions: Strategy, Repository, Observer, Decorator, Builder, and more.
20. **SOLID Principles** — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.
21. **Mapping** — Convert between domain objects and DTOs using AutoMapper or manual projection to avoid over-exposing internals.
22. **Logging** — Use `ILogger<T>` with structured logging (Serilog, NLog) and log levels; never use `Console.WriteLine` in production.
23. **Tuples and Records** — Tuples for lightweight multi-value returns; records for immutable data with value equality.
24. **Lambda Expressions** — Concise anonymous functions with `=>` syntax, the backbone of LINQ and delegate usage.
25. **Async and Await** — Non-blocking I/O with `async`/`await`; always propagate `CancellationToken`, avoid `.Result` and `.Wait()`.
26. **Pattern Matching** — Use `switch` expressions, `is` patterns, and positional patterns for expressive branching logic.
27. **Ternary Operator** — Replace simple if/else with `condition ? a : b` for concise inline expressions.
28. **Null-Coalescing Operators** — Use `??` for null fallbacks and `??=` to assign only when null.
29. **Pure Functions** — Functions with no side effects and deterministic output — easier to test and reason about.
30. **First-Class Functions** — Treat functions as values: pass them as arguments (`Func<>`, `Action<>`), return them, store them.
31. **Immutability** — Prefer immutable types (`record`, `readonly`) to prevent accidental mutation and simplify concurrency.
32. **Higher-Order Functions** — Functions that accept or return other functions; the foundation of functional-style C#.
33. **Nullable Reference Types** — Enable `<Nullable>enable</Nullable>` to get compile-time warnings for potential null dereferences.
34. **Pipelining** — Chain operations so the output of one feeds into the next, improving readability of data transforms.
35. **Events and Event Handling** — Use `event`, `EventHandler<T>`, and delegates to implement the observer pattern.
36. **Authentication and Authorization** — Use ASP.NET Core middleware: `AddAuthentication`, `AddAuthorization`, `[Authorize]`, policies, and claims.
37. **Domain-Driven Design (DDD)** — Model software around business domains using Entities, Value Objects, Aggregates, and Domain Events.
38. **Data Transfer Objects (DTOs)** — Decouple your API contract from internal domain models; prevents over-posting and over-fetching.
