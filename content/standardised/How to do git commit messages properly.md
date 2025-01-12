## Structure of a goof [[Git]] Commit Message

1. **Subject Line**
   - Keep it short (50 characters or less).
   - Use the imperative mood (e.g., "Fix bug" instead of "Fixed bug").
   - Capitalize the first letter.
   - Do not end with a period.

2. **Body (Optional)**
   - Separate from the subject line with a blank line.
   - Explain the "what" and "why" of the changes, not the "how".
   - Wrap text at 72 characters.

3. **Footer (Optional)**
   - Include references to issues or pull requests (e.g., "Closes #123").
   - Add any additional notes or metadata.

### **Good Examples**:

1. **Fix a Bug**  
   ```
   Fix incorrect login redirection
   The login redirection was leading to an unauthorized page after successful login. 
   This fix ensures users are redirected to their dashboard upon successful authentication.
   ```
   
2. **Add a New Feature**  
   ```
   Add search functionality to the user dashboard
   Introduced a search bar in the user dashboard, allowing users to quickly find relevant information within their profile.
   ```
   
3. **Update Documentation**  
   ```
   Update README to include new API endpoints
   Added details about the newly added API endpoints for user registration and password recovery in the README file.
   ```
   
4. **Refactor Code**  
   ```
   Refactor data fetching logic in the dashboard
   The data fetching logic was consolidated into a reusable service to improve maintainability and reduce duplication.
   ```
   
5. **Add Unit Tests**  
   ```
   Add unit tests for the authentication service
   Implemented unit tests for the login and registration methods to ensure robust coverage of authentication functionality.
   ```

### **Bad Examples**:

1. **Too Vague**  
   ```
   Update
   ```
   *This commit message doesn’t provide any meaningful context.*

2. **Incomplete Explanation**  
   ```
   Fix bug
   ```
   *This doesn’t explain the *what* or *why*, making it unclear to someone reviewing the code.*

3. **Too General**  
   ```
   Changed stuff
   ```
   *“Changed stuff” is not informative and doesn’t provide clear insight into what was actually modified.*

4. **No Context**  
   ```
   Fixed issue
   ```
   *No context is provided about what the issue was, making it difficult for others to understand the change.*

5. **Overly Short**  
   ```
   Remove unused variable.
   ```
   *The message could be expanded to include more context about why the variable was removed and what impact it had.*

---

### **Tips Expanded**:

- **Be Descriptive**: Commit messages should give a clear understanding of the changes. Describe what was changed, *why* it was changed, and *how* (if necessary).
- **Focus on One Change**: Avoid including unrelated changes in a single commit. Each commit should represent one logical unit of work.
- **Use Active Voice**: Avoid passive voice. Focus on the subject doing something (`Add`, `Fix`, `Implement`).
- **Wrap Text Appropriately**: Ensure lines don’t exceed 72 characters for better readability in Git log and discussions.
- **Be Concise**: Subject lines should be short (preferably under 50 characters), clear, and to the point without unnecessary detail.

---

### **Common Pitfalls** to Avoid:

- **Too Vague**: Commit messages like "Update" or "Fix bug" provide no actionable information.
- **Too Long**: Descriptive, yes, but avoid overly lengthy messages that become difficult to scan quickly.
- **No Context**: A good commit message should allow anyone reviewing it to understand the change without needing additional context.