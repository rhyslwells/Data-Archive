In [[standardised/GSheets]] I want to use query, but I also want to remove certain rows based on a range of keys , can I do this ?
### **1. Use `FILTER` Inside `QUERY` (ArrayFormula Workaround)**

Since `QUERY` does not support dynamic `NOT IN`, you can first filter out the excluded keys using `FILTER`, then pass the result to `QUERY`:

```excel
=QUERY(FILTER(A1:D, ISNA(MATCH(A1:A, X1:X10, 0))), "SELECT Col1, Col2, Col3, Col4", 1)
```

- `FILTER(A1:D, ISNA(MATCH(A1:A, X1:X10, 0)))`: Removes rows where column A matches any value in `X1:X10`.
- `QUERY(..., "SELECT Col1, Col2, Col3, Col4", 1)`: Runs a query on the filtered data.
