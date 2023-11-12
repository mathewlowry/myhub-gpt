For the experiments to be meaningful, I need to compare several approaches in each experiment, which requires the creation of several files:

- Basic inputs
	- Collection 1: this is a URL
	- [[Prompt 1 - newsletter]]
- **Summariser 0** is the original Summariser, written off the cuff for the ChatGPT pilot without much thought. It creates very short summaries and so serves as our "baseline Summariser" (see postscript).
	- [[C-1_s-0]] was created using Summariser 0 (ie short summaries of the Collection 1 notes)
	- hence [[c-1_s-0-response-p-1]]: what ChatGPT returns when sent [[C-1_s-0]] and asked Prompt 1
- **Summariser 1** (see [[summarisers in summary#^29496d]])
	- [[C-1_s-1-150]]: the content ChatGPT received, created using Summariser 1 set to 150 words
	- [[c-1_s-1-150-response-p-1]]: what ChatGPT returns when sent C-1-S-1-150 and asked Prompt 1
- **AllNotes**: to test if and how Summarisers affect the quality of ChatGPT's response, we need to apply the Prompt to the entirety of the notes, as well:
	- [[C-1_allnotes]] contains the entirety of the notes in Collection 1, created by taking the [Collection's RSS feed](https://myhub.ai/rss/@mathewlowry/?tags=creativity&types=like&timeframe=anytime&quality=all&tags=innovation) and applying [[rss to clean notes prompt]]
	- [[c-1_allnotes-response-p-1]]: what ChatGPT returns when sent C-1-AllNotes.md and asked Prompt 1
- finally, the analysis: [[Experiment 1 analyses]], itself written with the help of ChatGPT ([[experiment 1 analysis chatgpt execsummary]]).