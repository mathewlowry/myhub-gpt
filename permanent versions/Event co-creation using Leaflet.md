# Event co-creation using Leaflet

**This page focuses on using [Leaflet](https://leaflet.pub/) - one implementation of [standard.site](https://standard.site/) - for event co-creation.**

It was written in support of [[Co-creating your physical event with your online community|Event co-creation on the Atmosphere]], and uses as an example a short experiment I'm doing in the run up to the [ATProto.science conference](https://atproto.science/events/atmosphere2026/),
so if you landed on this page directly, you might want to check out the parent post for the wider context.

*(Note: This is version 2 of this sub-page. Version control in footer.)*

## Getting My Head Around Leaflet

[Leaflet.pub](https://leaflet.pub/) is one of the three originators of standard.site. To be honest it took me a little while to get my head around Leaflet, and [there's still a chance that I've got something wrong](https://bsky.app/profile/mathewlowry.eurosky.social/post/3mf5iro2v5s2g), which is one reason why this is one of my experimental, multiple-version posts.
### Basic Leaflet Components

You can do everything from simply publishing a standalone page (aka "looseleaf") right through to creating a Leaflet Publication, within which there are Pages, within which you can embed subpages, which appear to the right of the page:

![[leaflet-components-1.png]]

The above diagram shows (top-left to bottom-right):

* a publication ("ATProto.science") listing one Page: the agenda
* The Agenda Page (with a large chunk cut for length reasons) largely composed of embedded Subpages
* One of those subpages, open to the right
### Interaction and Sharing Options

Things get really interesting when you want to interact with this content - users can both comment on posts *and* share image-quotes to their followers on Bluesky:

![[leaflet-components-2.png]]

This second diagram shows:

* A traditional comment button at the bottom which opens a standard comment field to the right (top right)
* a small pop-up when the user selects some text, giving additional options:
	* comment on the selection (the selected text appears above the user's comment)
	* share the link to the exact location selected ([try it](https://atproto2026.leaflet.pub/3mevfbw7r522w/l-quote/019c60e7-6d9d-7773-a1b3-6521afff8f21~31_4-31_87#019c60e7-6d9d-7773-a1b3-6521afff8f21~31_4))
	* image-quote-post: Leaflet creates a Bluesky post for you featuring a link to the (sub)page and an *auto-generated image* of the selected text and its immediate neighbourhood.

Below, you can see that after I image-quote-posted my pithy comment to Bluesky, the page got a **Mentions feed** showing all Bluesky conversations about the page:

![[leaflet-mentions3.png]]

**Anyone visiting any Leaflet page can thus engage via the comments or jump to the relevant conversations on Bluesky.**

Note: personally I would prefer a single unified stream of comments & mentions, rather than Leaflet's two separate streams, but it's possible that there are good reasons for Leaflet's approach.

And as a quick aside: 

* The image-quote-post feature reminds me of early integration between the Medium blogging platform and Twitter. However, that was one app choosing to inter-operate with another, and it only lasted a year or two. When that feature was removed there was absolutely nothing anyone could do about it. 
* But if Leaflet removed image-quote-post, someone else could simply create another app which has it, and which can work with all existing standard.site content. **The inter-operability is guaranteed by the protocol.**
### Subscribing and Discussing

**That same interoperability is why anyone with a DID can subscribe to any Leaflet publication, and *any other app can see that subscription*.** 

And that enables all standard.site apps to do all sorts of interesting things - for example:

* the dedicated [**Leaflet reader**](https://leaflet.pub/reader) not only shows you posts from Leaflet publications you subscribe to but also from anything you subscribe to on [pckt.blog](https://pckt.blog/read), *another* standard.site app
* the [**Leaflet Reader Bluesky custom feed**](https://bsky.app/profile/did:plc:btxrwcaeyodrap5mnjw2fvmz/feed/subscribedPublications) means you can keep up with your standard.site subscriptions via *any* Bluesky app (Bluesky, Blacksky, Anisota, Deck.Blue...)
* there's even a [**Leaflet *Quotes* Bluesky custom feed**](https://bsky.app/profile/did:plc:btxrwcaeyodrap5mnjw2fvmz/feed/bsky-leaflet-quotes) which shows quote-posts from all Leaflet Publications (unlike the "Reader" custom feed, this one's not customised to you... I think).
* and [your leaflet posts can appear in your personal blog](https://www.pfrazee.com/leaflets/3mbnbdt4bas2a), if you build the latter on the Atmosphere - i.e., you can blog on Leaflet to get additional reach, and still show your posts on your own blog. Because it all resides on your PDS - the content's *yours*.

## So what does this mean for event co-creation?

**Publishing provisional and final event items in this way brings greater interactivity and reach, while simplifying your CMS.**

### More interactive features

As far as I can see, your audience we'll be able to:

* comment on the event item after logging in with their DID 
* share selections from the page to their Bluesky audiences without having to log in at all
* discover all comments and Bluesky conversations from the event item
* subscribe to only those event items that interest them, so you're not flooding your users' inboxes with every notification from across the entire event programme
* follow those conversations, and be alerted to new posts, using their Bluesky app, or their Leaflet reader, or even a dedicated app you embed on your site and/or provide for their phones.

### A simpler CMS

**And you don't have to build much yourself.**

Despite offering additional features I've never seen on an event co-creation website, the actual CMS becomes pretty simple, because you're farming out most of the interactive features to the Atmosphere. But you will need:

* a CMS which can publish using standard.site 
* a labeller: a lightweight ATProto service that attaches signed status labels to event items. 

**The labeller is the key change between this and the previous version of this post.** The previous approach reflected the CMS-oriented paradigm I picked up from building websites for over 30 years, and involved storing submitted proposals in the website CMS, pushing them to the user's PDS only when organisers promoted it to provisional status. 

But this is incompatible with the core ATProtocol principle of content sovereignty, so instead we put the event items onto the proposer's PDS from the outset. What changes is the label attached to it by the Jury, with the event website's CMS reading that label to decide what to display, where and to whom.

The following diagram shows how an event item in your website's provisional programme is created, labelled and published using standard.site and an event labeller:

![[event-cocreation-stdsite-v4.png]]

It shows user account creation and event item submission workflows:

* a user joins the community, becoming **Member 1** (*top left*). If s/he already has a DID, or opts in for getting one:
	* the DID is included in their public profile and the site CMS
	* s/he is given a label, so that anyone subscribing to the Labeller knows that she is a member of this community (the label is also used in the custom feed, below)
* Member 1 uses a site form (*top*) to **propose an event item**: a record is created in the CMS, but the content itself is published on Member 1's PDS (*centre*) as an event item with the label "**`event/proposed`**". Note: 
	* the website does not show this content to anyone, although it is all publicly visible via the user's PDS. 
	* the Organising Jury *can* view this content via a dedicated CMS-driven page which allows them to change the label
* The Organisers' Jury assesses Member 1's proposal, likes it, and changes the item's label: to "**`event/provisional`**". This makes the event item appear in the Provisional programme, visible to anonymous website visitors (*bottom right*).

Some final notes (not shown in image):

* Rejected proposals simply have their label negated, removing them from public views without deleting content from the member's PDS.
* Any edit of an event item can trigger a Jury review using something called a strong reference.
### Better reach

**Moreover, you're also getting a huge reach bonus.**

The following diagram shows what can happen next, now that the event item is visible on the site in the events Provisional programme:

![[event-cocreation-leaflet-reach-v4.png]]

Under "REACH" (*bottom-right*):

* as soon as the event item appears in in the Provisional programme:
	* it also appears in standard.site indexers, as well as event subscribers' feeds on across both standard.site *and* Bluesky apps
	* an automatic Bluesky post is published to Member 1's followers (if s/he opted in, [as explored in Berlin](https://mathewlowry.medium.com/how-newsrooms-scientific-institutions-governments-can-best-use-bluesky-ee97d840a058)); 
	* this post in turn appears in the event's Bluesky custom feed, reaching that audience.
* any Visitor with a DID can **mention or quote-post** the event item to their Bluesky followers. Their post appears:
	* on the event item itself, where others can follow it to Bluesky to join the conversation there
	* in the event's Bluesky custom feed (unless they manually delete the automatically placed hashtag).
* when community Member 2 **comments** on the event item:
	* if they have a DID, they can opt to auto-share that comment to their Bluesky followers; 
	* this post *also* appears in the event's custom feed.

There's a bit "REACH" to the *left*: because Members are labelled as community members, any of their Bluesky posts appear in the event's custom feed if they *also* includes the event hashtag (and the member opted in).

**Up to:** [[Co-creating your physical event with your online community|Event co-creation on the Atmosphere]]


---
## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: (2026-02-21)
	- added labeller, thanks to [Emelia](https://bsky.app/profile/thisismissem.social) 
- version control
    - this is version: 2
    - this is the current version: [[Event co-creation using Leaflet]]
    - here is the previous version: [[Event co-creation using Leaflet 1]]