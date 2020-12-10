/*
  define types for getting the last type in a tuple type,
  so we can get the type of the last parameter given.
*/
/** Get the length of a tuple type */
type GetLength<original extends any[]> = original extends { length: infer L } ? L : never
/** Decrement a number literal type by 1 */
type Prev<T extends number> = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62][T];
/** Get the type of the last type in a tuple type */
type TypeOfLastElement<T extends any[]> = T[Prev<GetLength<T>>];

/** The return type if the given type T is a function, T if it is not a function. */
type ReturnTypeIfFunction<T> = T extends (...params: any[])=>any ? ReturnType<T> : T

/**
 * return undefined if any of the given values are nullish,
 * otherwise return the last given value (return value if it is a function).
 * 
 * This may be used to simplify dependencies in svelte dynamic statements.
 */
export function depend<T extends any[]>(...values: T): ReturnTypeIfFunction<TypeOfLastElement<T>> {
    if (values.length < 1) return undefined;

    for (let val of values) {
        if (!val) return undefined;
    }

    const lastVal = values[values.length - 1];
    if (typeof lastVal === "function") {
        return lastVal();
    } else {
        return lastVal;
    }
}