
In this experiment I'm going to try and combine techniques developed in as many of the previous ones as possible, using the same content:

* **Collection 10:** [the stuff I like this year](https://myhub.ai/@mathewlowry/?quality=all&types=like&timeframe=this_year) - just 5 resources, as of 2024-01-09
	* C-10-0: [URL: stuff I like this year](https://myhub.ai/@mathewlowry/?quality=all&types=like&timeframe=this_year)
	* [[C-10-fullnotes]]
* **Process**: I threw the best part of my kitchen sink at this one, just to see what would happen if I followed this process using both the summarised and full notes versions of the collection, with the fullnotes sent to both chatgpt3.5 and chatgpt4:
	* first, [[Prompt 1 - newsletter]] to create a summary
	* then, [[prompt 2c - themes and resources visualised]] to generate some visualisations of the themes running through these articles. 
	* using this to identify topics of interest (preferably open source AI) and using elements of [[prompt 2e - framework]] to explore further
	* create a blog post: the visualisation is the main image, and the text explains it (prompt to be created)
* **Full responses:** 
	* [[C-10-S-0-response 1]], from which I have extracted:
		* newsletter: [[C-10-S-0-extract-newsletter 1]]
		* final resource & theme visualisations: : [[C-10-S-0-response-conceptmap3.jpeg]]
		* 2 versions were then created of a blog post: 
			* first effort: [[C-10-S-0-response-extract-blogpost-1 1]]
			* I then asked for "*greater depth, using quotes from all relevant articles wherever relevant, and ensuring each reference to an article is linked to its URL.*": [[C-10-S-0-response-extract-blogpost 2 1]]
		* I then challenged ChatGPT's bullshit about how AI creates bullshit, and it rather meekly agreed: "*The fact that the URL provided is fabricated emphasizes the importance of ensuring the reliability of AI-generated information. It raises concerns about the potential for chatbots or AI models to generate persuasive yet unsubstantiated text*"
	* putting the **full notes collection** ([[C-10-fullnotes]]) through ChatGPT3.5, and using wherever possible identical prompts, gives [[C-10-fullnotes-response-gpt35 1]], from which I have extracted: 
		* newsletter: [[C-10-fullnotes-3-5-extract-newsletter]]
		* visualisations: I had ChatGPT create 6 different visualisations, and I'm happy with none of them, so they remain embedded in [[C-10-fullnotes-response-gpt35 1]]
		* blogposts
			* [[C-10-fullnotes-response-gpt35-extract-blogpost1 1]]
			* [[C-10-fullnotes-response-gpt35-extract-blogpost2 1]]
	* putting the **full notes collection** ([[C-10-fullnotes]]) through **ChatGP4,** and using wherever possible identical prompts, gives: [[C-10-fullnotes-response-gpt4]], from which I have extracted:
		* newsletter: [[C-10-fullnotes-gpt4-extract-newsletter]]
		* visualisations: I had ChatGPT create 4 different visualisations, but none of them were any better than those previously created, so they remain in [[C-10-fullnotes-response-gpt4]]
		* blogposts
			* [[C-10-fullnotes-response-gpt4-extract-blogpost1]]
			* [[C-10-fullnotes-response-gpt4-extract-blogpost2]]
			* [[C-10-fullnotes-response-gpt4-extract-blogpost3]]
* Analyses: 
	* Using Summariser 0 (ie [[C-10-S-0-response 1]]):
		* the newsletter was boring, wooden and repetitive - it didn't even try, for example, to play the two articles on "bullshit" together. I should have pushed back and asked for better, but the main goal was for me to get an overview of the articles to inform the next stage (visualisations). 
		* visualisations: there was an improvement from 1 to 3, but frankly the underlying analysis was insufficiently insightful for these to be of much use
		* comparing the blog posts: the second was an improvement textually, but it made up URLs, despite having them in its memory (unless they'd passed out the token window?)
	* Using my full notes through ChatGPT3.5 vs ChatGPT4: 
		* GPT4's newsletter is objectively better 
			* 3.5's version writes a 1-para intro before summarising each article separately, with barely any connections between them, then a conclusion.
			* GPT4's gives us a 1-para intro followed by a 5para overview and a conclusion. The overview's paragraphs link together better.
		* Both versions of GPT produced roughly similar results. My previous conclusion - that these visualisations appear more interesting/useful than they actually are - remains unchanged
		* GPT4's newsletter is objectively better
			* after (as requested) introducing the subject (open source) and summarising the Mistral announcement, it was more able to address how the 4 other articles were relevant to open source
			* on the other hand, while I asked it to "Write in a more journalistic, less academic style" it instead wrote something closer to a Mistral press release
			* moreover, it really stretched to find anything relevant to OS in one of the articles. [My notes](https://myhub.ai/items/i-trained-chatgpt-on-my-notes-to-create-content-heres-what-happened) on this article do not "vividly illustrate the practical benefits of open-source AI". This is a borderline hallucination, but it's the sort of thing that can be useful if it helps you consider a connection that wasn't actually present in the original content... *if* you spot it.
	* Conclusion: I'll need some time to digest this, as while the GPT4 outputs were clearly better, I'm not sure they are 100x better, while GPT4 costs 100x more.

