---
creation date: 2026-08-24 11:34
modification date: 236 August 2026 11:34:51
---
# ReadingQ: building my first Obsidian plugin with Claude Code

**If your first reaction is to dogpile me for using AI to create code for personal use, please hold your nose and read to the end.**

*(Notes: This is version 1 of this post; more details and version control in the footer.)

## But first, why this plugin? 

I've been organizing my reading-thinking-writing-publishing-sharing process using a [content pipeline](https://medium.com/the-mission/why-you-need-a-personal-content-strategy-ff05c84fccfd) for well [over 10 years](https://medium.com/better-humans/manage-the-firehose-or-it-will-manage-you-791097bc53e2). I've barely had to tweak it: resources arrive in curated inboxes, which I scan to select content for my Reading Queue; then they're read, annotated, tagged and published as [Stuff I Like](https://myhub.ai/@mathewlowry/?quality=all&types=like&timeframe=anytime), with most also informing the [Stuff I Think or Do](https://myhub.ai/@mathewlowry/?quality=all&types=do&types=think&timeframe=anytime) precisely because I spent that time annotating them. 

The *tools* I use to manage and move knowledge through that pipeline, however, have evolved many times: Pocket & Raindrop, delicious & diigo, ifttt & Tumblr, *Obsidian & MassiveWiki, MyHub, Medium*, Twitter & Facebook, *LinkedIn, Bluesky & Leaflet*  have all played their part. Those in italics still do.

Throughout those years, the weakest link in the pipeline has remained unchanged: getting from *adding* something to my Reading Queue to actually *reading* it. This is not a tool problem, as an article I just dug up from my Reading Queue points out:

> "*a bookmark is a promise you make to a version of yourself who never shows up... capturing gives you the exact dopamine hit that thinking is supposed to give you, minus the work*" - [The Rise and Fall of the Second Brain](https://medium.com/health-science/the-rise-and-fall-of-the-second-brain-30d164b56750), Chris Ng, 6 August 2026.

A few weeks ago I would never have been able to find that article - my Reading Queue was a Raindrop account, so the only pipeline content I could actually find was the stuff I'd already read, annotated and tagged. 
## How the RQManager plugin works

**But I saw Chris' article just after I set up my plugin, so I shared it to my Obsidian vault, not Raindrop.** 

Here's what happens:

* I was using a mobile phone, where "Share to Obsidian" gives me 3 options, one of which is is to append the URL to the bottom of my vault's daily note. I designed my daily note using [Templater](https://community.obsidian.md/plugins/templater-obsidian), so Chris' URL appeared under the last heading ("*shared from apps*") 
	* (note: if I had been using a browser, I've configured [Obsidian Web Clipper](https://obsidian.md/clipper) to do the same thing with a keystroke)
* sometime later that day my plug-in was activated, either by me opening Obsidian on either of my PCs, or triggering it manually from my phone
* it sent a chunk of Chris' article to Claude, which compares it to my project list (a semantically rich file in my Obsidian vault) and returns one or more **project tags**. The above article, for example, was tagged #productivity, which is how I found it as I wrote this post before actually processing it fully
	* (note: if no project can be found, it returns #tagme)
* my plugin then turns the entire line into a [Task](https://community.obsidian.md/plugins/obsidian-tasks-plugin) with a deadline of tomorrow, applies the project tag(s) and the #readme tag to it, and moves it up one to the penultimate section of my daily note ("Added to readme today")
* as a result, the URL appears as a task in today's daily note and:
	* tomorrow's daily note, where it appears under "to read today" (thanks to the deadline and my daily note template)
	* in a central Reading Queue thanks to the Tasks plugin, where it can be easily filtered by tag (that's how I found Chris' article)
	* in each relevant project's ToDo list (a section of each project's Map of Content), thanks to the project tag and the Tasks plugin.

## What it doesn't fix

**This plugin doesn't solve the underlying problem:** devoting more time to reading and annotating the content on my Queue, as that's where I actually learn and generate many of my ideas. 

But it's still an improvement: reading queue content now appears everywhere relevant throughout my notes, making it more likely I will find that time; *and* Queued content is more accessible to the rest of my content pipeline because it's auto-tagged, something I've wanted for over 10 years.

## What's next

**But the real benefit of the exercise was that I've learnt how to improve my own pipeline tools, rather than adopting and configuring someone else's. Anyone can.** 

So this is the beginning of a journey, which I'm taking with Loki, my personal knowledge management AI assistant, created as a result of [Peter Kaminiski](https://peterkaminski.ai/)'s generosity. If you'd like your own AI assistant that lives in your notes, learns as you work and helps you build whatever you need, you can [get started for free](https://peterkaminski.ai/pkai-agent/), although I highly recommend becoming a [PKAI Insider](https://insiders.peterkaminski.ai/). 

Reading Queue Manager is actually the first step in revamping MyHub. 
I've wanted to improve collective intelligence by giving anyone who wants one a content pipeline, complete with a Hub for sharing content publicly, for many years. Since becoming atproto-pilled, however, I want these pipelines integrated into the Atmosphere. The idea is to offer both a revamped MyHub.ai platform *and* a local-first toolkit, providing credible exit from MyHub for each stage of the pipeline. My Reading Queue Obsidian plugin is a first step towards that local-first toolkit, but anything I create with AI will only ever be a proof of concept. If I can show there's enough interest to raise development funding, their first destination will be someone who actually knows what they're doing with the code.

And before you condemn me for using AI, remember:

* this is **personal code**, a few Markdown files in a directory inside an Obsidian vault on 2 PCs and a phone: I'm not releasing it to the world, I'm not committing to maintain it, and it doesn't matter that the code isn't elegant 
* this could not exist otherwise: I'm not a developer, and I'm sick and tired of describing systems I'll never see.

All that said — if anyone wants it, I'm happy to pass it across. It's very simple If you use Obsidian, so feel free to hit me up and I'll send you the files.

But by the time you read this, my plugin will almost certainly have evolved. 



---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: (2026-02-21)
	- n/a 
- version control
    - this is version: 1
    - this is the current version: [[Permanent version template]]
    - here is the previous version: n/a


