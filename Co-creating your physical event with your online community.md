**Revisiting some of the basic techniques for building online communities I've developed over the years in the light of the Atmosphere's potential.**

*(Notes: This is an early draft. As explained in [this newsletter edition](https://mathewlowry.medium.com/exploring-ai4communities-newsletter-6365b2716bb1), I am publishing these early versions as I develop my thoughts in the hope that constructive comments will help me finish the post. More version control in the footer.)*

I built the very first online community of practice for the European Commission in 2002 (and [blogged about it in 2009](https://myhub.ai/items/building-communities-with-event-in-a-box)). I discovered, almost by accident, that **online event co-creation** helps you leverage your event to boost your online community, and use your online community to run a more successful event.

These and other online communities were to be my bread and butter for the following ~10 years, and then started dying off as the conversation moved to Twitter and Facebook. The problem was that Twitter and Facebook didn't share, and took the oxygen out of these web-based online communities.

> Twitter and Facebook didn't share... But the situation is now changing

But the situation is now changing, as I argued last November in Berlin: the ATProtocol means "[social media can support, not undermine, online communities](https://mathewlowry.medium.com/how-newsrooms-scientific-institutions-governments-can-best-use-bluesky-ee97d840a058)), because we can **integrate our website-based online communities with global social media networks.**

Where my Berlin presentation focused on magnifying online communities with custom feeds, however, I now want to explore what technologies like [standard.site](https://standard.site/) can contribute. Hence the first, exploratory experiment I'm running for [atproto.science 2026](https://atproto.science/events/atmosphere2026/) - a side event to AtmosphereConf - at the end of March. So if you're coming to Vancouver, let me know and we'll compare notes.
## Event co-creation in brief

Event co-creation means involving your community in the definition of the event's content. Members' involvement can take several forms:

- submitting formal proposals for workshops, individual speeches, networking sessions, etc (call them **"event items"**).
- commenting on “provisional” event items (published for discussion by the community, but not yet in the final programme - see below) to help Organisers identify which generate the most interest
- online discussions amongst organisers, proposers and attendees to combine good proposals to create better event items.

This does much more than help Organisers identify the most interesting Submissions - **it is where Members discover other Members with similar interests, and encourages them to network online *before* they meet face to face**. 

By the time people actually do meet, therefore, they will have been discussing the event content for the preceding months, and so **will know exactly Who they want to meet and What they're going to talk about** (as well as When and Where, thanks to the messaging & coffee table booking systems we also built into the site).
### Benefits for attendees

What we discovered back in 2002 was that **most conference attendees were very keen on this approach**. Why is not hard to understand - as an attendee:

* getting a place in the conference programme:
	* means you're **helping set the agenda** of the event 
	*  increases your **visibility.** 
* the online discussions before the event
	* also raises your visibility and develops your network
	* help you discover the people you should meet in the limited time you have available on the day, and make them want to meet you.

### Benefits for Organisers

The most obvious benefits for the organisers are that this approach:

* ensures the event actually reflects the interests of the attendees, 
* is more valuable to each Member in terms of networking.

**But it also turns each member into an ambassador**: being selected for the provisional programme, after all, is a very good reason to promote the event to all of your friends, so they can support it.

Finally, it **injects massive energy into your online community,** which can support your organisation's work throughout the year. It's therefore really useful to see event co-creation as an integral part of your community strategy - using event co-creation for your annual event, for example, means the community you assemble for this year's event can come back to take part in the discussion about next year's event, and so on.
## How: Key milestones

**The trick is to get started early.** 

A good process for an event held at T=0 looks something like this: 

* T-6 months: launch your event website with the simple "save the date," follow us on social, and subscribe to the newsletter messages, so that you can then follow up with your followers and subscribers for...
* T-5 months: launch your open call - in a traditional event co-creation process, users describe themselves as they join your community so that they can propose ideas for the event programme (workshops, speeches, papers, presentations, networking sessions, etc. - it's up to you)
	* If you already have a community then your existing members should be able to simply compose and submit the proposal.
	* while those who have not yet joined your community now have a very good reason to do so.
	* In both cases it helps enormously if your members are submitting ideas directly into your website content management system, not some separate system (online polling tools,  Google Sheets, etc.)
* T - 4 months. Close the call, and read the proposals:
	* Mark the bad ones as rejected and inform their authors.
	* Mark the others as provisional. Importantly, there should be more provisional ideas than you actually have room and time for.
* T-minus 3.5 months: publish the Provisional Programme, thus opening the **event co-creation discussion phase**
	* invite your community members to comment and rate the ideas
	* Encourage people with similar ideas to combine forces.
* T-2 months: close the event co-creation discussion phase by publishing the final programme - basically this means 
	* Rejecting some more ideas, and informing the authors
	* Changing the status of the others from provisional to final.
* T-2 - event: continue to encourage the conversation around the final programme.

Of course you don't need to follow those dates exactly, but it is important that people know what the final programme is one or two months before the event so they can make logistics arrangements. For those first co-created events 25 years ago, in fact, we launched the event website 8-9 months before the event because we had several phases of discussion:

* a first call at T-6 asked people to submit ideas for workshops or individual presentations for the Conference Programme (which was a mix of science and policy)
* when we finalised the Conference programme we opened a second co-creation phase in T-3, for the Networking Programme, which focused on networking scientists together across Europe and took place in and around the exhibition. The people who didn't "make the cut" for the conference were encouraged to present networking event proposals, which most of them found them more valuable for their purposes.

The last time I was involved we had over 8,000 comments on the provisional networking programme in the month of August, 2026.
## Why look to the Atmosphere?

I've built websites with event co-creation several times since 2002. Each time, all of the interactivity was built into the website's content management system, which was as a result pretty complex.

Today I'm exploring if and how the website could integrate atproto to both simplify the CMS and integrate event co-creation into the global social media conversation, ensuring better engagement. 
### Identity crisis?

But wouldn't this also restrict that conversation to people who have an ATProto digital identity (DID; in most cases a Bluesky account)? 

Yes... unless, when somebody joins your community and doesn't have a DID or a Personal Data Server (PDS), **you simply gave them one as part of their account creation process.**

From their perspective, they're creating an account on your website so that they can get involved in your event. But you're actually giving them: 

* a digital identity they can use on your website *and every other ATProto app on the Atmosphere*, from BlueSky through to Stream.Place
* and a PDS to store their content, which they can move elsewhere whenever they want.

This is therefore for organisations who have decided to integrate their online operations - both website and social media - with the Atmosphere.
### Benefits 

The first, obvious benefit is **personal sovereignty** - your users store their content on their PDS (either the one they already had, or the one you're providing them), which means they maintain ownership over it. You don't own them, so treat them well.

The other main benefit, of course, is **engagement reach**: your event content can become an integral part of the Atmosphere, a social network of over 40 million people. We'll explore how this looks below.
## How?

### Meet the standard

Firstly, note that you probably won't need to publish every single page of your website onto the Atmosphere - you simply decide which content types are stored on your users' PDSs and published onto your website with a little extra code, called a lexicon.

And that lexicon already exists: **standard.site**. As a developer who discovered it less than 2 weeks before writing this put it:

> "Within a week, my site had actually turned ATProto into a CMS. I could make posts, update them, or delete them, and all the while these updates are broadcasted to a network that anyone could index" - [Standard.site: the Publishing Gateway](https://stevedylan.dev/posts/standard-site-the-publishing-gateway/) (Steve Dylan)

Steve shows how flexible and extensible the basic standard.site architecture is by adding a new lexicon for comments. Other developers have done something similar (eg [First thoughts on integrating with standard.site](https://isaaccorbrey.com/ramblings/first-thoughts-on-integrating-with-standard-site)), while on [leaflet.pub](https://leaflet.pub/) - one of the three originators of standard.site - users can both comment on posts *and* share quotes to their followers on Bluesky:

* comments appear in a dedicated comment stream
* all Bluesky mentions of the post (including the quote-posts) appear in a dedicated Mentions feed on the page.

* image

Note that if you have a DID you can subscribe to any Leaflet publication, which is where Leaflet gets very clever, as they have two dedicated custom feeds on Bluesky:

* [Leaflet Reader](https://bsky.app/profile/did:plc:btxrwcaeyodrap5mnjw2fvmz/feed/subscribedPublications): shows you all the posts from the Leaflet publications you're subscribed to - ie, an enewsletter, but in social form (it's not clear to me whether those Bluesky posts appear as mentions on the Leaflet publications' posts themselves?)
* [Leaflet Quotes](https://bsky.app/profile/did:plc:btxrwcaeyodrap5mnjw2fvmz/feed/bsky-leaflet-quotes) not clear if this shows quote-posts only from publications you've subscribed to, or all of the quote-posts on all of the publications, whether you've subscribed to them or not? 

### Public data

But this is also where we have to tackle the fact that **everything on the ATmosphere is public**. 

In Vancouver I look forward to hearing about the development of permissioned data, but for this version of this post I'm operating on the assumption that submitted event items need to be stored in the website CMS *only*, and are pushed onto users' PDSs and displayed to anonymous website users only when they have reached at least provisional status.

The following diagram uses colour coding to show where the content resides:

* image

It shows 

* someone joins the community, and is added to its custom feed
* the community member uses a form to submit an event item as a proposal to the conference programme - this record is only accessible to organisers using the CMS 
* an organiser reads it and changes the record's status to provisional
	* the record appears on the website, with the actual content stored on the user's PDS
	* triggering an automatic share to the users' followers
* from this point onwards validated community members can comment on the event item, and  can opt to auto-share that comment to their followers on Bluesky.
* anyone with a DID can also quote-post text from the event item to their Bluesky followers in the same way as with Leaflet, above. These posts also appear on the event item. 

However, I would prefer to not have two streams as on Leaflet. Instead, a single unified stream of comments and bluesky mentions would be preferable.

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- none, as this is the first 
- version control
    - this is version: 1
    - this is the current version: [[Co-creating your physical event with your online community]]
    - here is the previous version: n/a