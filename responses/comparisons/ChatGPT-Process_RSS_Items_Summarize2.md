# Process RSS Items, Summarize Output

#### You:
 am going to give you some RSS items and you will process it as follows: 
1. Extract the title of the RSS item. 
2. Extract the URL from the <link> item, not the <guid> item, and removes any utm suffix 
3. Extract the main content from the description section, taking care to not remove any content from description 
4. Remove any HTML tags within the main content. 
5. Preserve line breaks for paragraph breaks. 
6. Present the extracted title followed by the cleaned main content. 

Here is an example input item: 
<item> 
<guid>https://myhub.ai/items/originals-hidden-brain-npr</guid> 
<pubDate>Mon, 03 Dec 2018 12:07:34 CET</pubDate> 
<title>Originals | Hidden Brain : NPR</title> 
<link>https://www.npr.org/2018/08/20/640216385/you-2-0-originals?utm_source=pocket_reader</link> 
<description>In his new book, Originals: How Non-Conformists Move the World, Adam investigates who comes up with great ideas, how, and what we can do to have more of them....<br> originals are not the people with the deepest expertise. They're people with the broadest experience... really good at questioning the status quo...<p>Tags: creativity, innovation, management, top3pods, original</p></description> <category>creativity</category> <category>innovation</category> <category>management</category> <category>top3pods</category> <category>original</category> 
</item> 

And here is how I'd like you to process it: 
Originals | Hidden Brain : NPR https://www.npr.org/2018/08/20/640216385/you-2-0-originals 
In his new book, Originals: How Non-Conformists Move the World, Adam investigates who comes up with great ideas, how, and what we can do to have more of them.... originals are not the people with the deepest expertise. They're people with the broadest experience... really good at questioning the status quo...

And now here is the  first content I want you to process:
<item>
<guid>https://myhub.ai/items/so-you-think-president-trump-is-the-worst-case-scenario-some-thoughts-originally-on-my-oldblog-and-then-updated-on</guid>
<pubDate>Fri, 11 Mar 2016 06:29:04 CET</pubDate>
<title>Prepping for the AfterTrump</title>
<link>https://medium.com/@mathewlowry/prepping-for-the-aftertrump-bacf489fba41</link>
<image>
<url>https://myhub.ai/images/BLupuDO-MA6_crY3yp5kJ-LZMHM=/3733/width-251/%5E2019/11/18/7/7e5e1867aa4ef3323bf403f16d11a91btumblr_o48w0tGOhK1qa4p6bo1_1280.jpg</url>
<link>https://medium.com/@mathewlowry/prepping-for-the-aftertrump-bacf489fba41</link>
</image>
<description><p>&quot;So you think “President Trump” is the worst case scenario?&quot; - Some thoughts, originally on my oldblog and then updated on Medium: </p><p>Tags: politics, trump, publicsphere, fascism</p></description>
<category>politics</category>
<category>trump</category>
<category>publicsphere</category>
<category>fascism</category>
</item>
<item>
<guid>https://myhub.ai/items/unfair-comparisons-sotu-v-soteu</guid>
<pubDate>Wed, 09 Mar 2016 09:44:00 CET</pubDate>
<title>Unfair comparisons: #sotu v #soteu</title>
<link>https://myhub.ai/items/unfair-comparisons-sotu-v-soteu</link>
<image>
<url>https://myhub.ai/images/REXriDktJtCstPpEcstKO-Pn5NE=/12294/width-251/%5E2021/11/8/m/mediadumps260files201603unionspeeches.png</url>
<link>https://myhub.ai/items/unfair-comparisons-sotu-v-soteu</link>
</image>
<description><p><i>Imported from the Blogactiv.eu blogging platform, closed without warning in 2021. Links, images and embeds not guaranteed, and comments not displayed.</i></p><p><b>A short post on the financial costs of not having a European Public Sphere.</b></p><p>@voxdotcom did a 4-minute summary of Obama&#x27;s 2016 #sotu (State of the Union):</p><p></p><embed embedtype="media" url="https://www.youtube.com/watch?v=DygBfjNTHk4"/><p></p><p>Here in Brussels, the @EU_Commission did a <a href="http://ec.europa.eu/priorities/state-union-2015_en">&quot;Highlights&quot; video</a> of Juncker&#x27;s #SOTEU which, like all EC videos, cannot be embedded by popular Wordpress-based blogging platforms like this one (I&#x27;m sure they&#x27;ve got a good reason for this, right?).</p><p>Before you try, don&#x27;t waste your time comparing the two - you can&#x27;t. On the one you have something produced by a real media about a political speech on a necessarily low budget, viewed ~100,000 times; on the other you have something considerably more polished and edited, produced by the politician&#x27;s own team, viewed a little over 31,000 times.</p><p>What&#x27;s instructive is the fact that the Commission&#x27;s efforts were necessary at all - I&#x27;ve yet to see any &#x27;real media&#x27; bothering with a &#x27;best of #soteu&#x27;, although if someone can point me to one I&#x27;d be glad to add it here. If not, this does illustrate the cost of <i>not</i> having a functioning European public sphere - instead of relying on it to support and carry the debate, the Institutions must resort to increasingly expensive measures to get their message out. Quite apart from the cost to democracy, this stuff costs money to make.</p><h3>Further reading</h3><ul><li><a href="http://mathew.blogactiv.eu/2016/01/27/towards-a-21st-century-eu-communications-strategy/">Towards a 21st century EU Communications Strategy</a></li><li>There are a few resources tagged <a href="http://mathewlowry.tumblr.com/tagged/publicspace">public space</a> on my Hub, and absolutely loads tagged <a href="http://mathewlowry.tumblr.com/tagged/media">media</a>.</li><li>I share resources like these <a href="http://mathewlowry.tumblr.com/">on my Hub</a> (almost) every day and (in theory) every fortnight via my <a href="http://mathewlowry.tumblr.com/tagged/newsletter">newsletter</a> – why not <a href="http://mathewlowry.tumblr.com/subscribe">subscribe</a>?</li></ul><p></p><p>Tags: media, publicsphere</p></description>
<category>media</category>
<category>publicsphere</category>
</item>
<item>
<guid>https://myhub.ai/items/exploring-translated-syndication-at-future-media-lab-2016</guid>
<pubDate>Mon, 15 Feb 2016 09:12:00 CET</pubDate>
<title>Exploring Translated Syndication at Future Media Lab 2016</title>
<link>https://myhub.ai/items/exploring-translated-syndication-at-future-media-lab-2016</link>
<image>
<url>https://myhub.ai/images/ulOsvEnievz3YGpPTut7WCOeKYc=/12298/width-251/%5E2021/11/8/m/mediadumps260files201602Slide5.png</url>
<link>https://myhub.ai/items/exploring-translated-syndication-at-future-media-lab-2016</link>
</image>
<description><p><i>Imported from the Blogactiv.eu blogging platform, closed without warning in 2021. Links, images and embeds not guaranteed, and comments not displayed.</i></p><p><b>The afternoon session at Future Media Lab 2016 showed that while European media are warming to the idea of using advanced language technologies to share content across borders, their audiences are already well ahead of them.</b> </p><p><i>This is a repost from the </i><a href="http://www.futuremedialab.info/blog/exploring-translated-syndication-at-future-media-lab-2016?platform=hootsuite"><i>Future Media Lab blog</i></a><i> (and so matches its dryness) and covers a workshop led by a</i> <a href="http://mathew.blogactiv.eu/2015/11/09/back-to-euractiv-for-some-media-innovation/"><i>client</i></a><i>. </i> </p><p>The conference session explored the “Translation Syndication” concept, where media in different countries exchange, translate, localise and republish each other’s content, increasing both volume and depth of coverage cost-effectively. To media outsiders, this sounds like a no-brainer: today’s media is in crisis, and media working in different languages are not competitors, so why on Earth would they <i>not</i> exchange content and mutually boost their revenues? </p><p>The reality, of course, is far more complex. The few experiments to date, such as the (website-free) Leading European Newspaper Alliance and the (temporary) <a href="http://www.globaleditorsnetwork.org/cpn/">Climate Publisher’s Network</a>, have been extremely lo-tech and exploratory.</p><h3>Media trailing their own audience</h3><p>But data presented by Christophe Leclercq as he opened the session suggests that European audiences would like more:</p><embed embedtype="image" format="fullwidth" id="12296"/><blockquote>64% of the respondents to EurActiv’s recent Readership Survey (1790 responses, December 2015-January 2016) would like to see more translated articles from national media sources.</blockquote><p>But what, exactly, do we mean by translated articles? The survey showed that although 60% use Google Translate at work, under 20% are satisfied with machine translation only, even if it does give them an immediate result:</p><blockquote></blockquote><embed embedtype="image" format="fullwidth" id="12297"/><p><i>Almost 60% would prefer machine translation improved by a human being within ‘same day’ or ‘half day’ timescales.</i></p><h3>Enter Translated Syndication</h3><p>The basic idea behind Translated Syndication was then set out to the session participants, who then split into tables to workshop answers to three questions: how could it help their competitiveness; what are the obstacles; and what should institutions like the EU and media associations do to help? </p><p>The resulting process can be summarised as follows: </p><p></p><embed embedtype="media" url="http://www.slideshare.net/mathew.lowry/translated-syndication-workflow"/><p></p><p><i>1. Media in the Translated Syndication Platform share content to it direct from their CMS</i> <br/><i>2. Each article is automatically categorised by a ‘Relevance Engine’ …</i> <br/><i>3.… before being auto-translated and summarised.</i> <br/><i>4. As journalists in other media in the Platform prepare their articles, their CMS automatically presents a feed of relevant articles from across Europe, auto-translated and ready to use</i> <br/><i>5. They correct, localise and otherwise incorporate this content into their own publication, deepening their coverage and/or increasing their output.</i> </p><p>The resulting discussion was a good example of how a group can refine and develop an idea – the ‘Relevance Engine’ in Step 2, for example, emerged from two workshop tables, as did a wider spectrum of uses for the syndicated content, from simply sharing ‘journalistic research’ through to localising and republishing articles.</p><h3>Building trust is key</h3><p>Inevitably, trust emerged as a key issue: participating media will need to be sure that the content they are re-using comes from quality sources, particularly as the Platform may remove the articles’ surrounding context. Apart from applying appropriate Membership requirements, more than one participant suggested building a lightweight social network into the Platform, allowing journalists to message an article’s author to get the necessary background. As an added benefit, such a network would stimulate journalistic and commercial collaboration across Europe.</p><blockquote>“such a network would stimulate deeper journalistic collaboration across Europe”</blockquote><p>Similarly, trusting that the Platform handles copyright management would be crucial, particularly with so many freelancers working in media. Blockchains were floated as a possible solution here. Despite these reservations, each workshop table was clear that such a Platform would definitely improve their media’s competitiveness, and - unsurprisingly - called upon the EU to boost research funding in the field.</p><h3>Further reading</h3><ul><li><a href="https://medium.com/@mathewlowry/advanced-technologies-for-european-democracy-e3c3ecbbe996#.5113wt24m">Applying advanced language technologies to EU democracy</a></li><li>21 <a href="http://mathew.blogactiv.eu/tag/media/">posts tagged media</a> here, and another 230+ useful resources tagged <a href="http://mathewlowry.tumblr.com/tagged/media">media</a> on my Hub</li></ul><p></p><p>Tags: media, publicsphere, machine translation, multilingualism, syndicated-translation</p></description>
<category>media</category>
<category>publicsphere</category>
<category>machine translation</category>
<category>multilingualism</category>
<category>syndicated-translation</category>
</item>

#### ChatGPT:
Here are the processed RSS items you provided:

**Item 1: Prepping for the AfterTrump**
Prepping for the AfterTrump <https://medium.com/@mathewlowry/prepping-for-the-aftertrump-bacf489fba41>

"So you think “President Trump” is the worst case scenario?" - Some thoughts, originally on my oldblog and then updated on Medium:
Tags: politics, trump, publicsphere, fascism

**Item 2: Unfair comparisons: #sotu v #soteu**
Unfair comparisons: #sotu v #soteu <https://myhub.ai/items/unfair-comparisons-sotu-v-soteu>

Imported from the Blogactiv.eu blogging platform, closed without warning in 2021. Links, images and embeds not guaranteed, and comments not displayed.
A short post on the financial costs of not having a European Public Sphere.
@voxdotcom did a 4-minute summary of Obama's 2016 #sotu (State of the Union):
Here in Brussels, the @EU\_Commission did a "Highlights" video of Juncker's #SOTEU which, like all EC videos, cannot be embedded by popular Wordpress-based blogging platforms like this one (I'm sure they've got a good reason for this, right?).
Before you try, don't waste your time comparing the two - you can't. On the one you have something produced by a real media about a political speech on a necessarily low budget, viewed \~100,000 times; on the other you have something considerably more polished and edited, produced by the politician's own team, viewed a little over 31,000 times.
What's instructive is the fact that the Commission's efforts were necessary at all - I've yet to see any 'real media' bothering with a 'best of #soteu', although if someone can point me to one I'd be glad to add it here. If not, this does illustrate the cost of not having a functioning European public sphere - instead of relying on it to support and carry the debate, the Institutions must resort to increasingly expensive measures to get their message out. Quite apart from the cost to democracy, this stuff costs money to make.
Further reading:
Towards a 21st century EU Communications Strategy
There are a few resources tagged public space on my Hub, and absolutely loads tagged media.
I share resources like these on my Hub (almost) every day and (in theory) every fortnight via my newsletter – why not subscribe?
Tags: media, publicsphere

**Item 3: Exploring Translated Syndication at Future Media Lab 2016**
Exploring Translated Syndication at Future Media Lab 2016 <https://myhub.ai/items/exploring-translated-syndication-at-future-media-lab-2016>

Imported from the Blogactiv.eu blogging platform, closed without warning in 2021. Links, images and embeds not guaranteed, and comments not displayed.
The afternoon session at Future Media Lab 2016 showed that while European media are warming to the idea of using advanced language technologies to share content across borders, their audiences are already well ahead of them.
This is a repost from the Future Media Lab blog (and so matches its dryness) and covers a workshop led by a client.
The conference session explored the “Translation Syndication” concept, where media in different countries exchange, translate, localize and republish each other’s content, increasing both volume and depth of coverage cost-effectively. To media outsiders, this sounds like a no-brainer: today’s media is in crisis, and media working in different languages are not competitors, so why on Earth would they not exchange content and mutually boost their revenues?
The reality, of course, is far more complex. The few experiments to date, such as the (website-free) Leading European Newspaper Alliance and the (temporary) Climate Publisher’s Network, have been extremely lo-tech and exploratory.
Media trailing their own audience
But data presented by Christophe Leclercq as he opened the session suggests that European audiences would like more:
64% of the respondents to EurActiv’s recent Readership Survey (1790 responses, December 2015-January 2016) would like to see more translated articles from national media sources.
But what, exactly, do we mean by translated articles? The survey showed that although 60% use Google Translate at work, under 20% are satisfied with machine translation only, even if it does give them an immediate result:
Almost 60% would prefer machine translation improved by a human being within ‘same day’ or ‘half day’ timescales.
Enter Translated Syndication
The basic idea behind Translated Syndication was then set out to the session participants, who then split into tables to workshop answers to three questions: how could it help their competitiveness; what are the obstacles; and what should institutions like the EU and media associations do to help?

1. Media in the Translated Syndication Platform share content to it direct from their CMS
2. Each article is automatically categorized by a ‘Relevance Engine’ …
3. … before being auto-translated and summarized.
4. As journalists in other media in the Platform prepare their articles, their CMS automatically presents a feed of relevant articles from across Europe, auto-translated and ready to use
5. They correct, localize and otherwise incorporate this content into their own publication, deepening their coverage and/or increasing their output.
   The resulting discussion was a good example of how a group can refine and develop an idea – the ‘Relevance Engine’ in Step 2, for example, emerged from two workshop tables, as did a wider spectrum of uses for the syndicated content, from simply sharing ‘journalistic research’ through to localizing and republishing articles.
   Building trust is key
   Inevitably, trust emerged as a key issue: participating media will need to be sure that the content they are re-using comes from quality sources, particularly as the Platform may remove the articles’ surrounding context. Apart from applying appropriate Membership requirements, more than one participant suggested building a lightweight social network into the Platform, allowing journalists to message an article’s author to get the necessary background. As an added benefit, such a network would stimulate journalistic and commercial collaboration across Europe.
   “such a network would stimulate deeper journalistic collaboration across Europe”
   Similarly, trusting that the Platform handles copyright management would be crucial, particularly with so many freelancers working in media. Blockchains were floated as a possible solution here. Despite these reservations, each workshop table was clear that such a Platform would definitely improve their media’s competitiveness, and - unsurprisingly - called upon the EU to boost research funding in the field.
   Further reading:
   Applying advanced language technologies to EU democracy
   21 posts tagged media here, and another 230+ useful resources tagged media on my Hub
   Tags: media, publicsphere, machine translation, multilingualism, syndicated-translation

Please note that for the sake of brevity, I've only included the title, URL, and main content without HTML tags for each item. If you have more items to process or need further assistance, please let me know.
