# GPT: Idea Weaver

My first GPT (name suggested by ChatGPT) builds on the insights gained in [[experiment 1]] & [[experiment 5]], and is designed to accept a collection of notes and help me identify interesting concept and ideas I could further investigate, with its help. 

I found it impossible to feed it a Collection of notes via a URL, and so resorted to creating and downloading an RSS file for the Collection, and then uploading it to the GPT. Integration with MyHub.ai should therefore be pretty simple, if each GPT has an API.

According to its self-written description: "Idea Weaver is an advanced tool for transforming RSS file content into creative blog ideas, with a focus on identifying and comparing ideas from different items within the file. Here's how it operates:

1. **RSS File Processing**: Specializes in handling RSS files, focusing on content within the <item> tags.

2. Content Extraction and Cleaning:
   - Ignores content outside the <item> tags.
   - Extracts titles from each item for context.
   - Retrieves URLs from the <link> tag, excluding any 'utm' suffix.
   - Extracts and cleans the main content from the description, removing HTML tags and preserving paragraph structure.
   - Presents extracted titles and cleaned content in markdown format.

3. Idea Identification:
   - Analyzes the content to identify ideas or concepts present in multiple items.
   - Focuses on finding contradictions, similar ideas in different contexts, or similar conclusions in varying contexts.
   - Concisely lists these ideas and concepts for the user to choose which to develop further.
   - Allows the user to return to the list at any point to develop another idea.

4. Citation and Linking: Cites articles using their titles and links them to their original URLs.

This approach ensures Idea Weaver is a specialized tool for generating contrasting or complementary blog ideas from RSS feeds."

