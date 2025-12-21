
# CoCoMo geoselection problem

*(You're reading a draft, published using the [permanent versions pattern](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e), where I publish a string of versions as I develop my thoughts in the hope of collecting constructive criticism and ideas along the way. Links to the latest and previous versions, if any, are in the footer.)*

This technical issue is only relevant if you are an organisation who wants to fund [[CoCoMo]] to support startups in a certain geographic area - eg, the French government supporting French startups by shouldering the legal content moderation burden for 12 months per startup.

## Problem in a nutshell

The problem is this: CoCoMo can only be applied to content by lexicon (knowledge of which is assumed). So if a European startup launches an app using lexicon X and contracts CoCoMo to moderate its content, CoCoMo will moderate all the content in Lexicon X anywhere, whether it was created using the company's app or not.

This is why Bluesky Social PBC actually moderates content for all apps which use the Bluesky lexicon - these apps can basically "free ride" on their moderation service.

Now it should be pointed out that there's a massive efficiency factor here: once CoCoMo identifies as a piece of content as problematic, all apps benefit from this. So this is a super-efficient way of supporting multiple companies working with the same lexicon.

But there's a problem *from the perspective of our French funding agency*:

* an Australian company, Kangaroo Social, launches an app, Roos!, with a new lexicon, Kanga. It gets traction. They have to pay for moderation. 
* A European company forks the code to launch their own app based on the Kanga lexicon, and contracts CoCoMo.
* The Aussies have a head start and 90% of the content in the Kanga lexicon comes from their users.
* But CoCoMo moderates all of it, without distinguishing between the "source app". So the European company's CoCoMo service moderates content created by the Australian app, and the Australians don't have to pay for moderation at all - they free-ride the French company.

Another scenario: 

* seeing the French government support startups in this space, Kangaroo Social sets up a French company to fork the code and launch Wombat Social, using the same lexicon. 
* Wombat Social never leaves alpha - the company exists solely to contract CoCoMo.... via a grant from the French government, which is now paying to support an Australian company, which free-rides the French government.

## Solutions?

The only public conversation about CoCoMo cost sharing is [How should we fairly split the costs of commons moderation across producer and consumer apps?](https://discourse.atprotocol.community/t/how-should-we-fairly-split-the-costs-of-commons-moderation-across-producer-and-consumer-apps/122) explored a few ideas, but not from the perspective of a funding agency wanting to support startups in a specific geographic area. 

---

This is part of [[A Eurosky project workprogramme]].

**Revision Notes:** This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  . Version control:

- this is version: 1, 2025-12-21
- this is the current version: [[CoCoMo geoselection problem]]
- here is the previous version: N/A
