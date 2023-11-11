# GPT: Idea Weaver

![[ideaweaver.jpg]]

## Background

My first GPT (name suggested by ChatGPT) builds on the insights gained in [[experiment 1 - newsletter]] & [[experiment 5 - ideator]], and is designed to accept a collection of notes and help me identify interesting concept and ideas I could further investigate, with its help. It was first used in [[experiment 6 - ideator GPT]].

I found it impossible to feed it a Collection of notes via a URL, and so resorted to creating and downloading an RSS file of the Collection, which I then uploaded to the GPT (the [[rss to clean notes prompt]], developed earlier, therefore played a part as well). Integration with MyHub.ai should therefore be pretty simple, if each GPT has an API, although the cost of uploading files to a GPT is apparently far higher than simply sending text to ChatGPT (to be confirmed).

## What it does

According to its self-written description: 

*"Idea Weaver is an advanced tool for transforming RSS file content into creative blog ideas, with a focus on identifying and comparing ideas from different items within the file. Here's how it operates:*

### RSS File Processing
Specializes in handling RSS files, focusing on content within the *item* tags.

### Content Extraction and Cleaning
* Ignores content outside the *item* tags.
* Extracts titles from each item for context
* Retrieves URLs from the *link* tag, excluding any 'utm' suffix
* Extracts and cleans the main content from the description, removing HTML tags and preserving paragraph structure
* Presents extracted titles and cleaned content in markdown format.

### Idea Identification
- Analyzes the content to identify ideas or concepts present in multiple items.
- Focuses on finding contradictions, similar ideas in different contexts, or similar conclusions in varying contexts.
- Concisely lists these ideas and concepts for the user to choose which to develop further.
- Allows the user to return to the list at any point to develop another idea.

### Citation and Linking
Cites articles using their titles and links them to their original URLs.

*This approach ensures Idea Weaver is a specialized tool for generating contrasting or complementary blog ideas from RSS feeds."*

