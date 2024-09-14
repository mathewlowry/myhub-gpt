
## experiment round 1: identify optimal length for Summariser S-1

Several experiments until optimal S-1 length found.

How: 
* create a collection of notes: C-n (url) (C-1, C-2...)
	* we already have "short summaries" created using Tim's simple prompt (Summariser 0) to chatgpt right now
	* but I cant send their notes
* manually create file of their notes: "C-n-AllNotes"
	* using [[rss to clean notes prompt]]
* manually create summaries using Summariser S-n of length X1 of their notes: "C-n-S-n-X1"
* use Prompt-P-x (P-1, P-2)
	* x = 1
	* in myhub: use short summaries (S-0) to create response to Prompt-P-x: C-n-S-0-response-P-x
	* in chatgpt:  
		* send "C-n-AllNotes" with Prompt P-x to create C-n-AllNotes-response-P-x
		* send "C-n-S-n-X1" with Prompt P-x to create C-n-S-n-X1-response-P-x
	* compare quality of reply to P-x operating on Collection-C-n: which one does best?
		* Responses (evaluation input files):
			* C-n-P-x-S-0-response
			* C-n-AllNotes-response-P-x
			* C-n-S-n-X1-response-P-x
		* Evaluation file: C-n-P-x-evaluation
	* if AllNotes is best 
		* then 
			* X2 = X1 + 20% 
			* repeat with X2
			* better than AllNotes?
				* y: exit
				* n: X3=X1+40%, repeat
	* Once having found the optimal length for Prompt 1, use that in round 2
## experiment round 2
We have the optimal length for Summariser 1 (S-1-X) using Prompt 1. 
* Test it against the other Prompts (P-x = P-2, P-3, ...): is C-1-S-n-X-response-P-x as good as C-1-AllNotes-response-P-x?
* Test it using other Collections (C-n = C-2, C-3, ...)

Take stock, design round 3

## experiment process 2
* As above but add variation by Summary-X-*N* (Summary-X-1, Summary-X-2...)
	* Summary created of X length using summariser N




----
# Backup

## Comparisons

### Collection C-1  
Description: 
total notes: 
- short summaries: URL: 
* [[Collection-C-1-AllNotes]]
- [[Collection-C-1-Summaries-X]]

![[Prompt 1 title]]

#### Responses
* in myhub: using short summaries - [[Collection-C-1-P-1-response-shortsummaries]]
* in chatgpt: using 
	* AllNotes: [[Collection-C-1-P-1-response-AllNotes]]
	* Summaries of length X: [[Collection-C-1-P-1-response-Summaries-X]]

#### evaluation

## Comparisons

### Collection C-1  
Description: 
total notes: 
- short summaries: URL: 
* [[Collection-C-1-AllNotes]]
- [[Collection-C-1-Summaries-X]]

![[Prompt 1 title]]

#### Responses
* in myhub: using short summaries - [[Collection-C-1-P-1-response-shortsummaries]]
* in chatgpt: using 
	* AllNotes: [[Collection-C-1-P-1-response-AllNotes]]
	* Summaries of length X: [[Collection-C-1-P-1-response-Summaries-X]]

#### evaluation


----
# Archive

### Collection C-1 

| prompt             | Goal | Short Summaries                           | Full note                             | 250Note                            | Comparison                    |
| ------------------ | ---- | ----------------------------------------- | ------------------------------------- | ---------------------------------- | ----------------------------- |
| [[Prompt 1 title]] | goal | [[Collection 1 - Prompt1-ShortSummaries]] | [[Collection 1 - Prompt 1-FullNotes]] | [[Collection 1 - Prompt 1-XNotes]] | [[Collection 1 - Prompt 1 - Comparison]] |
| [[Prompt 2 title]]       | goal     |  [[Collection 1 - Prompt2-ShortSummaries]]               |   [[Collection 1 - Prompt 2-FullNotes]]        |  [[Collection 2 - Prompt 2-XNotes]]       |    [[Collection 1 - Prompt 2 - Comparison]]        |                   |      |                                           |                                       |                                    |                               |

## Prompt 1 & Collection 1

![[Prompt 1 title]]

### Short Summaries
Input - Collection 1: URL
[[Collection 1 - Prompt1-ShortSummaries]]

### Full Notes
Input: [[Collection 1 - Full Notes]]
[[Collection 1 - Prompt 1-FullNotes]]

### X Notes
Input: [[Collection 1 - X Notes]]
[[Collection 1 - Prompt 1-XNotes]]

## Prompt 2 & Collection 1

![[Prompt 2 title]]

### Short Summaries
Input - Collection 1: URL
[[Collection 1 - Prompt2-ShortSummaries]]

### Full Notes
Input: [[Collection 1 - Full Notes]]
[[Collection 1 - Prompt 2-FullNotes]]

### X Notes
Input: [[Collection 1 - X Notes]]
[[Collection 1 - Prompt 2-XNotes]]

