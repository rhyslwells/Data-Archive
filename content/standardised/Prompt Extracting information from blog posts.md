---
tags:
  - prompt
---
Prompt Extracting information from blog posts

You are an expert in summarizing and analyzing online content. Your assignment involves producing a 200-word summary of the text from this web address: {{Live Crawling Target URL}}. The text from URL {{Live Crawling Target URL}} is:

The resulting summary must be around 200 words.

Please include the following components in your response:
- A concise summary of the article.
- A list of key points as bullet points under the "important" section.
- Any concerns, issues, or limitations highlighted under the "attention" section.
- Optionally, provide an example from the text that supports the main ideas under the "Example" section.
- Formulate two or more follow-up questions related to the article.

Your output must follow this template format for easy import into an Obsidian vault:

>[!Summary]
> {{200-word summary of the URL content}}

>[!important]
> - {{Key point 1}}
> - {{Key point 2}}

>[!attention]
> - {{Issue 1}}
> - {{Issue 2}}

>[!Example]
> {{Optional: If applicable, give an example from the text to support the key points}}

>[!Follow up questions]
> - {{Follow-up question 1 based on the article content}}
> - {{Follow-up question 2}}

>[!Link]
>