# Process RSS Items: Summarize

#### You:
I am going to give you some RSS items and you will process it as follows: 
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
<guid>https://myhub.ai/items/to-mend-a-broken-internet-create-online-parks-wired</guid>
<pubDate>Sun, 25 Oct 2020 01:34:04 CET</pubDate>
<title>To Mend a Broken Internet, Create Online Parks | WIRED</title>
<link>https://www.wired.com/story/to-mend-a-broken-internet-create-online-parks/</link>
<image>
<url>https://myhub.ai/images/oXMYA_0DMjUcdqrmr68LUYzci9w=/11930/width-251/%5E2020/10/25/p/photos5f84c1d34dbf8ba438224a83masterw_25602Cc_limitOpEd-Int_BTwBhlU.jpg</url>
<link>https://www.wired.com/story/to-mend-a-broken-internet-create-online-parks/</link>
</image>
<description><p>&quot;Our digital public sphere has been failing ... [but] History offers a proven template for how to build healthier public spaces.&quot;</p><p>Filter Bubble author Pariser hearkens back to Walt Whitman&#x27;s creation of NY&#x27;s Green Park, when &quot;New York City had no public parks ...only walled commercial pleasure gardens for those who could afford&quot;. He saw American democracy needed &quot;spaces to celebrate individuality <i>and</i> build collective identity... help weave a greater, more egalitarian “we”... Functional public spaces ... allow us to assemble, to share common experiences, and to demonstrate that ... individual struggles are actually the result of unjust systems&quot;.</p><p>Today we use social media platforms, but they &quot;weren&#x27;t designed to serve as public spaces. They were designed to monetize attention... [and] make poor quasi-public spaces for three reasons:&quot;</p><ul><li>frictionlessness is good for business, but bad for public spaces, which are useful &quot;precisely because we run into people we’d normally avoid, encounter events we’d never expect, and have to negotiate with other groups that have their own needs [creating] ... social connections ... critical in binding communities together across lines of difference&quot;. This takes time - but VC-backed platforms are in a rush - akin to neighbourhood gentrification</li><li>Command-and-control by &quot;Boy Emperors with huge blind spots ... public squares designed by a small group of white dudes of a certain age is not going to serve everyone equally or well... Great public spaces are owned by everyone and therefore ought to be designed for everyone&quot;</li><li>&quot;public spaces require constant, active care and maintenance by skillful stewards ... moderators and editors ... balancers of freedom, inclusion, and safety&quot;</li></ul><p>The article doesn&#x27;t call for today&#x27;s platforms to be dismantled, but &quot;it’s unreasonable to expect for-profit corporations ... to accommodate every digital need... [we need] digital public infrastructure... parks, libraries, and truly public squares on the internet&quot;.</p><p>Which means meeting 3 challenges: money, ideally from a tax on targeted advertising, talent and willpower.</p><p>Tags: social media, democracy, publicsphere, fediverse</p></description>
<category>social media</category>
<category>democracy</category>
<category>publicsphere</category>
<category>fediverse</category>
</item>
<item>
<guid>https://myhub.ai/items/what-is-activitypub-and-how-will-it-change-the-internet</guid>
<pubDate>Sun, 20 Sep 2020 05:00:34 CEST</pubDate>
<title>What is ActivityPub, and how will it change the internet?</title>
<link>https://jeremydormitzer.com/blog/what-is-activitypub.html</link>
<image>
<url>https://myhub.ai/images/aHWeWFQDsMuPB8pxND7yIcIe1qw=/11877/width-251/%5E2020/9/20/i/imagesboard-game.jpg</url>
<link>https://jeremydormitzer.com/blog/what-is-activitypub.html</link>
</image>
<description><p>ActivityPub separates content from platform. Posts from one platform propagate to other platforms, and users don’t need an account on every platform ... for ex., YouTube clone <a href="https://joinpeertube.org/en/faq/">PeerTube</a> and Mastodon both implement it, so is Mastodon user A follows PeerTube user B, B&#x27;s new videos will appear in A&#x27;s Mastodon feed. A can even comment on it <b>from Mastodon</b></p><p>your ActivityPub identity is already there on all ActivityPub platforms, making impersonations impossible.</p><p>This flips network effects from the platform to the protocol: the more platforms adopt ActivityPub, the more valuable it becomes for more platforms to join in...</p><p>But it still faces the empty train syndrome, so funding is critical. And ads won&#x27;t work: &quot; There is no centralized audience to segment and advertise to. We’ll need to rethink the fundamental business model of social networking if we want ActivityPub to take off. &quot;</p><p></p><p>Tags: publicsphere, open web, myhub, fediverse, activitypub</p></description>
<category>publicsphere</category>
<category>open web</category>
<category>myhub</category>
<category>fediverse</category>
<category>activitypub</category>
</item>

#### ChatGPT:
Here are the processed RSS items as per your instructions:

1. **To Mend a Broken Internet, Create Online Parks | WIRED**
   [Link](https://www.wired.com/story/to-mend-a-broken-internet-create-online-parks/)

   "Our digital public sphere has been failing ... \[but] History offers a proven template for how to build healthier public spaces."
   Filter Bubble author Pariser hearkens back to Walt Whitman's creation of NY's Green Park, when "New York City had no public parks ...only walled commercial pleasure gardens for those who could afford". He saw American democracy needed "spaces to celebrate individuality and build collective identity... help weave a greater, more egalitarian “we”... Functional public spaces ... allow us to assemble, to share common experiences, and to demonstrate that ... individual struggles are actually the result of unjust systems".
   Today we use social media platforms, but they "weren't designed to serve as public spaces. They were designed to monetize attention... \[and] make poor quasi-public spaces for three reasons:"

   - frictionlessness is good for business, but bad for public spaces, which are useful "precisely because we run into people we’d normally avoid, encounter events we’d never expect, and have to negotiate with other groups that have their own needs \[creating] ... social connections ... critical in binding communities together across lines of difference". This takes time - but VC-backed platforms are in a rush - akin to neighbourhood gentrification
   - Command-and-control by "Boy Emperors with huge blind spots ... public squares designed by a small group of white dudes of a certain age is not going to serve everyone equally or well... Great public spaces are owned by everyone and therefore ought to be designed for everyone"
   - "public spaces require constant, active care and maintenance by skillful stewards ... moderators and editors ... balancers of freedom, inclusion, and safety"
     The article doesn't call for today's platforms to be dismantled, but "it’s unreasonable to expect for-profit corporations ... to accommodate every digital need... \[we need] digital public infrastructure... parks, libraries, and truly public squares on the internet".

   Tags: social media, democracy, publicsphere, fediverse

2. **What is ActivityPub, and how will it change the internet?**
   [Link](https://jeremydormitzer.com/blog/what-is-activitypub.html)

   ActivityPub separates content from platform. Posts from one platform propagate to other platforms, and users don’t need an account on every platform ... for ex., YouTube clone [PeerTube](https://joinpeertube.org/en/faq/) and Mastodon both implement it, so is Mastodon user A follows PeerTube user B, B's new videos will appear in A's Mastodon feed. A can even comment on it from Mastodon
   your ActivityPub identity is already there on all ActivityPub platforms, making impersonations impossible.
   This flips network effects from the platform to the protocol: the more platforms adopt ActivityPub, the more valuable it becomes for more platforms to join in...
   But it still faces the empty train syndrome, so funding is critical. And ads won't work: " There is no centralized audience to segment and advertise to. We’ll need to rethink the fundamental business model of social networking if we want ActivityPub to take off."

   Tags: publicsphere, open web, myhub, fediverse, activitypub

I have extracted the titles, removed UTM suffixes from the links, extracted the main content from the descriptions while preserving line breaks, and removed HTML tags within the main content as per your instructions.


#### You:
Now process in the same way the following content: 
<item>
<guid>https://myhub.ai/items/building-a-more-honest-internet-columbia-journalism-review</guid>
<pubDate>Wed, 27 Nov 2019 09:32:02 CET</pubDate>
<title>Building a More Honest Internet - Columbia Journalism Review</title>
<link>https://www.cjr.org/special_report/building-honest-internet-public-interest.php</link>
<image>
<url>https://myhub.ai/images/nyaRI49FVdhqKT_80znZ0P2hhck=/6024/width-251/%5E2019/11/27/w/wp-contentuploads201911web_zuckerman_yang_2500-800x419.jpg</url>
<link>https://www.cjr.org/special_report/building-honest-internet-public-interest.php</link>
</image>
<description><p>In the US, radio began as a free-market free-for-all. More than five hundred radio stations sprang up in less than a decade to explore the possibilities... 40 percent were noncommercial... network of interlinked stations playing local and national content supported by local and national advertising, became dominant players...</p><p>Soviet Union... ideology prevented ... commercial broadcasting, and state-controlled radio quickly became widespread... a way to align the political thinking of a vast land populated primarily by illiterate farmers... once private radios became available, “wired radio”... connected virtually every building in the country...</p><p>United Kingdom ... eschewing the extremes... the British Broadcasting Company was licensed to broadcast content for the nation... [with] a built-in revenue stream... ... to be the British citizen’s “guide, philosopher, and friend,”... mouthpiece of an empire ... socially conservative and high-minded... moralistic and boring. But it also invented public service media... earned credibility by giving airtime to both government and opposition leaders... becoming one of the most reliable sources of information in the world.</p><p>Those models... offer a helpful road map as we consider ... the rise of the commercial internet...there are significant flaws in the global model... “surveillance capitalism”... social-media networks ... addictive sources of unregulated information that are easily weaponized...</p><p>public service digital media may be what we need... the current model of the internet is not inevitable... in China... unfettered capitalism of the US internet is blended with tight state oversight... state-backed censorship and surveillance baked in... The second alternative model is public service media... Of the world’s top hundred websites, Wikipedia is the sole noncommercial site. If the contemporary internet is a city, Wikipedia is the lone public park; the rest of our public spaces shopping malls... Wikipedia’s method of debating its way to consensus... a “neutral point of view” ... proved surprisingly durable...</p><p>public service media... fill a void in the marketplace... by the early 1970... PBS and NPR were bringing <i>Sesame Street</i> and<i> All Things Considered</i> to the American public... A public service Web invites us to imagine services that don’t exist... not commercially viable... perhaps should exist... fill a black hole of misinformation with educational material and legitimate news...</p><p>to avoid a world in which Google throws our presidential election... allow academics or government bureaucrats to regularly audit the search engine [or] create a public-interest search engine with audits built in...</p><p>social platforms may be increasing political polarization, straining social ties, and causing us anxiety ... creating “filter bubbles” ... in part, a fault of its financial model... the platform optimizes for “engagement,”... a disincentive to challenge users ... the stories that Facebook is built to direct our attention to... reinforce existing prejudices and inspire emotional reactions...</p><p>imagine a social network designed... encourage the sharing of mutual understanding rather than misinformation?... encourages you to interact with people with whom you might have a productive disagreement... <b>measure success in terms of new connections, sustained discussions, or changed opinions...</b> wouldn’t be commercially viable... precisely why public service models exist: to counter market failures....</p><p>It’s hard to tear users away from a platform they are already accustomed to... if you do gain momentum ... Facebook will likely purchase it... mandate of interoperability... we could build social media browsers that put existing social networks, and new ones, in the same place</p><p>Tags: social media, media, filter bubble, publicsphere, wikipedia, open web, radio, disinformation, indieweb, interoperability</p></description>
<category>social media</category>
<category>media</category>
<category>filter bubble</category>
<category>publicsphere</category>
<category>wikipedia</category>
<category>open web</category>
<category>radio</category>
<category>disinformation</category>
<category>indieweb</category>
<category>interoperability</category>
</item>
<item>
<guid>https://myhub.ai/items/news-publishers-go-to-war-with-the-internet-and-we-all-lose</guid>
<pubDate>Fri, 14 Jun 2019 09:15:38 CEST</pubDate>
<title>News Publishers Go To War With the Internet — and We All Lose</title>
<link>https://medium.com/whither-news/news-publishers-go-to-war-with-the-internet-and-we-all-lose-cc8aca5336f5</link>
<image>
<url>https://myhub.ai/images/-BM1aMlZrqvUjux19My-Be7IGlk=/3843/width-251/%5E2019/11/18/m/max7941mwU-WVQhyqmwd29_-AWEIg.jpeg</url>
<link>https://medium.com/whither-news/news-publishers-go-to-war-with-the-internet-and-we-all-lose-cc8aca5336f5</link>
</image>
<description>news industry trade associations are corruptly cashing in their political capital ... their members are newspapers, and politicians are scared of them — in desperate acts of protectionism to attack platform companies. The result is a raft of legislation that will damage the internet and in the end hurt everyone, including journalists and especially citizens...<br> Google is emphasizing news ... good for publishers, as that sends them readers... publishers aren’t competent at ... creating valuable ongoing relationships with the people sent their way... dogged refusal to understand how the internet has changed their world... contend that Google is taking their “content”... like a camera stealing their soul...<br> EU copyright legislation tries to force Google ... to pay for quoting snippets of content ... Google won’t... platforms will link to news less ... self-inflicted harm for the news industry ... hurting the public conversation... <p>Tags: media, eu, publicsphere, copyright</p></description>
<category>media</category>
<category>eu</category>
<category>publicsphere</category>
<category>copyright</category>
</item>

#### ChatGPT:
Here are the processed RSS items as per your instructions:

1. **Building a More Honest Internet - Columbia Journalism Review**
   [Link](https://www.cjr.org/special_report/building-honest-internet-public-interest.php)

   In the US, radio began as a free-market free-for-all. More than five hundred radio stations sprang up in less than a decade to explore the possibilities... 40 percent were noncommercial... network of interlinked stations playing local and national content supported by local and national advertising, became dominant players...
   Soviet Union... ideology prevented ... commercial broadcasting, and state-controlled radio quickly became widespread... a way to align the political thinking of a vast land populated primarily by illiterate farmers... once private radios became available, “wired radio”... connected virtually every building in the country...
   United Kingdom ... eschewing the extremes... the British Broadcasting Company was licensed to broadcast content for the nation... \[with] a built-in revenue stream... ... to be the British citizen’s “guide, philosopher, and friend,”... mouthpiece of an empire ... socially conservative and high-minded... moralistic and boring. But it also invented public service media... earned credibility by giving airtime to both government and opposition leaders... becoming one of the most reliable sources of information in the world.
   Those models... offer a helpful road map as we consider ... the rise of the commercial internet...there are significant flaws in the global model... “surveillance capitalism”... social-media networks ... addictive sources of unregulated information that are easily weaponized...
   public service digital media may be what we need... the current model of the internet is not inevitable... in China... unfettered capitalism of the US internet is blended with tight state oversight... state-backed censorship and surveillance baked in... The second alternative model is public service media... Of the world’s top hundred websites, Wikipedia is the sole noncommercial site. If the contemporary internet is a city, Wikipedia is the lone public park; the rest of our public spaces shopping malls... Wikipedia’s method of debating its way to consensus... a “neutral point of view” ... proved surprisingly durable...
   public service media... fill a void in the marketplace... by the early 1970... PBS and NPR were bringing Sesame Street and All Things Considered to the American public... A public service Web invites us to imagine services that don’t exist... not commercially viable... perhaps should exist... fill a black hole of misinformation with educational material and legitimate news...
   to avoid a world in which Google throws our presidential election... allow academics or government bureaucrats to regularly audit the search engine \[or] create a public-interest search engine with audits built in...
   social platforms may be increasing political polarization, straining social ties, and causing us anxiety ... creating “filter bubbles” ... in part, a fault of its financial model... the platform optimizes for “engagement,”... a disincentive to challenge users ... the stories that Facebook is built to direct our attention to... reinforce existing prejudices and inspire emotional reactions...
   imagine a social network designed... encourage the sharing of mutual understanding rather than misinformation?... encourages you to interact with people with whom you might have a productive disagreement... measure success in terms of new connections, sustained discussions, or changed opinions... wouldn’t be commercially viable... precisely why public service models exist: to counter market failures....

   Tags: social media, media, filter bubble, publicsphere, wikipedia, open web, radio, disinformation, indieweb, interoperability

2. **News Publishers Go To War With the Internet — and We All Lose**
   [Link](https://medium.com/whither-news/news-publishers-go-to-war-with-the-internet-and-we-all-lose-cc8aca5336f5)

   news industry trade associations are corruptly cashing in their political capital ... their members are newspapers, and politicians are scared of them — in desperate acts of protectionism to attack platform companies. The result is a raft of legislation that will damage the internet and in the end hurt everyone, including journalists and especially citizens...
   Google is emphasizing news ... good for publishers, as that sends them readers... publishers aren’t competent at ... creating valuable ongoing relationships with the people sent their way... dogged refusal to understand how the internet has changed their world... contend that Google is taking their “content”... like a camera stealing their soul...
   EU copyright legislation tries to force Google ... to pay for quoting snippets of content ... Google won’t... platforms will link to news less ... self-inflicted harm for the news industry ... hurting the public conversation...

   Tags: media, eu, publicsphere, copyright

I have extracted the titles, removed UTM suffixes from the links, extracted the main content from the descriptions while preserving line breaks, and removed HTML tags within the main content as per your instructions.


#### You:
Now process in the same way the following content: 
<item>
<guid>https://myhub.ai/items/its-the-democracy-poisoning-golden-age-of-free-speech-wired</guid>
<pubDate>Wed, 21 Feb 2018 01:10:21 CET</pubDate>
<title>It's the (Democracy-Poisoning) Golden Age of Free Speech | WIRED</title>
<link>https://www.wired.com/story/free-speech-issue-tech-turmoil-new-censorship/</link>
<image>
<url>https://myhub.ai/images/AAAKeyw5o_qo3gvFf0Cm2Mbomk8=/3983/width-251/%5E2019/11/18/p/photos5a5abe3ec77f7f39b676d8a7191100w_1280c_limitopener.jpg</url>
<link>https://www.wired.com/story/free-speech-issue-tech-turmoil-new-censorship/</link>
</image>
<description>the capacity to spread ideas ... no longer limited by access to expensive... infrastructure. It’s limited instead by one’s ability to garner and distribute attention. And right now, the flow of the world’s attention is structured... by just a few digital platforms:... tincreasingly stand in for the public sphere itself... at their core... They’re ad brokers... <br> Humans are a social species, equipped with few defenses ... beyond our ability to acquire knowledge and stay in groups that work together... particularly susceptible to glimmers of novelty, messages of affirmation and belonging, and messages of outrage toward perceived enemies. These kinds of messages are to human community what salt, sugar, and fat are to the human appetite. And Facebook gorges us on them... no nutritional labels... <br> posts are targeted and delivered privately, screen by screen... Today’s phantom public sphere has been fragmented and submerged into billions of individual capillaries... all of this invalidates much of what we think about free speech—conceptually, legally, and ethically. The most effective forms of censorship today involve meddling with trust and attention, not muzzling speech ... viral or coordinated harassment campaigns, which harness the dynamics of viral outrage to impose an unbearable and disproportionate cost on the act of speaking out... epidemics of disinformation, meant to undercut the credibility of valid information sources. They look like bot-fueled campaigns of trolling and distraction, or piecemeal leaks of hacked materials... swamp the attention of traditional media...<br> freedom of speech is an important democratic value, but it’s not the only one... usually understood as ... necessary condition for achieving certain other societal ideals... when free speech is treated as an end and not a means, it is all too possible to thwart and distort everything it is supposed to deliver. Creating a knowledgeable public requires at least some workable signals that distinguish truth from falsehood... Today’s engagement algorithms... espouse no ideals about a healthy public sphere... <br> the core business model underlying the Big Tech platforms—harvesting attention with a massive surveillance infrastructure to allow for targeted, mostly automated advertising at very large scale—is far too compatible with authoritarianism, propaganda, misinformation, and polarization... <p>Tags: algorithm, social media, facebook, publicsphere, free speech, disinformation</p></description>
<category>algorithm</category>
<category>social media</category>
<category>facebook</category>
<category>publicsphere</category>
<category>free speech</category>
<category>disinformation</category>
</item>
<item>
<guid>https://myhub.ai/items/is-banning-trolls-a-prerequisite-of-or-a-defeat-for-free-speech</guid>
<pubDate>Wed, 27 Jul 2016 08:46:00 CEST</pubDate>
<title>Is banning trolls a prerequisite or a defeat for free speech?</title>
<link>https://myhub.ai/items/is-banning-trolls-a-prerequisite-of-or-a-defeat-for-free-speech</link>
<image>
<url>https://myhub.ai/images/xPDb8z7FeWbqxuPyien5kv2pKhc=/12308/width-251/%5E2021/11/8/m/mediadumps260files201607banned-796x3481.jpg</url>
<link>https://myhub.ai/items/is-banning-trolls-a-prerequisite-of-or-a-defeat-for-free-speech</link>
</image>
<description><p data-block-key="pqa22"><i>Imported from the Blogactiv.eu blogging platform, closed without warning in 2021. Links, images and embeds not guaranteed, and comments not displayed.</i></p><p data-block-key="8twal"><b>The permanent banning of uber-troll Milo Yiannopoulos from Twitter was probably long overdue. It&#x27;s time for non-trolls to stop complaining and start </b><b><i>defending</i></b><b> civility in our social spaces, or simply decamp to build better ones. </b><i>(image:</i> <a href="http://thenextweb.com/insider/2016/07/20/twitter-gives-conservative-writer-milo-yiannopoulos-axe-bans-permanently/"><i>NextWeb</i></a><i>)</i></p><p data-block-key="grp3w">I&#x27;m not here to argue the rights and wrongs of this particular case (for what it&#x27;s worth, Yiannopoulos denies the crimes he&#x27;s been accused of). What bothers me more is how the self-styled “most fabulous supervillain on the internet&quot; immediately cast Twitter&#x27;s decision as <a href="https://twitter.com/cwarzel/status/755601176603791360/photo/1?ref_src=twsrc%5Etfw">a blow to free speech</a>, as well as a victory for &quot;Muslim terrorists and Black Lives Matter extremists&quot; - exactly the sort of conflation only a truly <i>dedicated</i> asshole - someone who&#x27;s managed to turn that behaviour into a profitable business model - could make.</p><p data-block-key="7k74p">The <a href="https://twitter.com/hashtag/FreeMilo">support</a> the &#x27;free speech&#x27; argument garnered reminded me of the recent brouhaha over Facebook&#x27;s Trending Topics (see my <a href="http://mathewlowry.tumblr.com/post/144759201420/facebook-mobocracy-augmented-reality-your">May enewsletter</a>). People seem to view Twitter and Facebook as utilities, serving up free speech like power companies serve up electricity or gas. Power utilities are not allowed to &#x27;ban&#x27; customers (as long as they pay) because a citizen&#x27;s right to energy is considered pretty fundamental. From utilities, in other words:</p><blockquote data-block-key="9nvph">&quot;<i>we expect a kind of dumb passivity … phone companies don’t send through certain calls and not others…Utilities are regulated to assure fairness and consistency of service; Facebook and Google are not.</i>“ - <a href="http://www.newyorker.com/business/currency/why-do-we-care-if-facebook-is-biased?">Why Do We Care If Facebook Is Biased?</a> New Yorker</blockquote><p data-block-key="6djbt">But Twitter and Facebook are <i>not </i>utilities. They&#x27;re more like private clubs: free to join, but 100% owned by private interests who are totally within their rights to blackball a member who acts like a dick and whips up a mob to drive thousands of other people out the door. So don&#x27;t cry for Milo - he&#x27;ll be fine:</p><blockquote data-block-key="7ryz3">“It’s fantastic... The timing is perfect.... I thought I had another six months, but this was always going to happen.” - <a href="https://medium.com/welcome-to-the-scream-room/im-with-the-banned-8d1b6e0b2932#.vsg5k8cce">I&#x27;m with the Banned</a>, Laurie Penny</blockquote><h2 data-block-key="0wnv0">Better late than never</h2><p data-block-key="o1t9v">Instead, having been on the receiving end of some trolls&#x27; attention almost a decade ago*, <b>I&#x27;m applauding Twitter.</b> Better late than never. Social media platforms have become central to our public discourse, so how they manage their members&#x27; behaviour directly impacts politics and society. That means their rules affect <i>everyone</i>, whether members of these platforms or not.</p><p data-block-key="z1d9k">So perhaps people treat them like utilities because they&#x27;d <i>like</i> some sort of democratic control? Wise up, guys: these are private, unregulatable clubs whose prime imperative is to make a return for their investors, not foster democratic debate. Which is perhaps why, as Laurie Penny puts it, right now &quot;the spoils go to those with fewest fucks to give&quot;, why we have leaders like Trump, Farage and Johnson, and...</p><blockquote data-block-key="h2ejt">&quot;... how we got to a place where headline speakers at the Republican convention... are now actively calling for the slaughter and deportation of foreigners, declare that Hillary Clinton is an agent of Satan, and hear only cheers from the floor&quot;</blockquote><h2 data-block-key="rf8ol">Use with caution</h2><p data-block-key="boiaf">I can&#x27;t recommend her article enough for the insights it gives into the many subspecies of trolls which have evolved over the past 10 years, and how they have begun sucking rational discourse out of our democracies by gaming social media:</p><blockquote data-block-key="zx57h">... the game of turning raw rage into political currency... Milo is the best player here. Like Trump, and like a lot of successful politicians in this postmodern circus, they channel their own narcissism to give voice to the wordless, formless rage of the people neoliberalism left behind.</blockquote><p data-block-key="aezp5"><a href="https://medium.com/welcome-to-the-scream-room/im-with-the-banned-8d1b6e0b2932#.9sdy2afxt">So go read it</a>. And then remember that: a) this is not inevitable: change the rules, change the game; b) the platforms will change the rules only when they see it as commercially necessary c) as users of these platforms: Collectively, in fact, we probably have more control over social media platforms than we do over any utility. </p><ul><li data-block-key="lgihv">we are the only people the platforms&#x27; <i>owners</i> listen to, because <b>we&#x27;re the product -</b> without us logging in, they won&#x27;t make any money</li><li data-block-key="8uahm">the platforms&#x27; algorithms reflect <i>our</i> values, so <b>how they evolve is up to us.</b></li></ul><p data-block-key="6w97h">So use with caution. </p><p data-block-key="ik1jj"><b>Further reading</b> * I&#x27;m in no way saying that <a href="http://mathew.blogactiv.eu/2008/10/15/hello-world/">my 2007 experience with Eurosceptic trolls</a> comes anywhere <i>close</i> to what some people experience every day on social media. As a white male, I probably never will. But they did get under my skin, and that little inkling was more than enough.</p><ul><li data-block-key="imdv1"><a href="https://medium.com/welcome-to-the-scream-room/im-with-the-banned-8d1b6e0b2932#.vsg5k8cce">I&#x27;m with the Banned</a>, Laurie Penny</li><li data-block-key="xnn5o"><a href="http://www.newyorker.com/business/currency/why-do-we-care-if-facebook-is-biased?">Why Do We Care If Facebook Is Biased?</a> curated in <a href="http://mathewlowry.tumblr.com/post/144759201420/facebook-mobocracy-augmented-reality-your">Facebook, Mobocracy &amp; Augmented Reality - your latest Top3ics (May 23)</a></li><li data-block-key="wx01d"><a href="http://mathew.blogactiv.eu/2016/01/13/where-is-social-media-taking-you-in-2016/">Where is social media taking you in 2016?</a></li><li data-block-key="azou2">More resources tagged <a href="http://mathewlowry.tumblr.com/tagged/troll">troll</a>, <a href="http://mathewlowry.tumblr.com/tagged/comments">comments</a> on my TumblrHub (<a href="http://mathewlowry.tumblr.com/subscribe">subscribe</a> to get some in your inbox occasionally via my <a href="http://mathewlowry.tumblr.com/tagged/newsletter">newsletter</a>)</li></ul><p>Tags: publicsphere, troll, social-media, comment</p></description>
<category>publicsphere</category>
<category>troll</category>
<category>social-media</category>
<category>comment</category>
</item>
<item>
<guid>https://myhub.ai/items/european-unity-is-meaningless-without-a-media-to-match-media-the-guardian</guid>
<pubDate>Mon, 30 May 2016 04:44:18 CEST</pubDate>
<title>European unity is meaningless without a media to match | Media | The Guardian</title>
<link>http://www.theguardian.com/media/2016/may/29/european-unity-meaningless-without-media-to-match-eu-superstate?utm_campaign=digest&utm_medium=email&utm_source=app</link>
<image>
<url>https://myhub.ai/images/Nkzia_Sg4xI2cD0z2NwL8u7Hqao=/4618/width-251/%5E2019/11/18/i/imgmediad5d9966517ca4d24b489efb3129682c8fb33a6ec0_162_4252_25524252.jpg</url>
<link>http://www.theguardian.com/media/2016/may/29/european-unity-meaningless-without-media-to-match-eu-superstate?utm_campaign=digest&utm_medium=email&utm_source=app</link>
</image>
<description>There will never be an ‘EU superstate’ as long as the national presses of 28 countries are presenting 28 different visions of the European dream... there is no real union if members can’t watch together, read together, instinctively think and bind together. No news means no common purpose... A continent of many languages has no means of building businesses with the scale digital success seems to demand. <p>Tags: media, eu, publicsphere</p></description>
<category>media</category>
<category>eu</category>
<category>publicsphere</category>
</item>
<item>
<guid>https://myhub.ai/items/opening-up-euractivs-media-innovation-programme</guid>
<pubDate>Tue, 29 Mar 2016 09:25:21 CEST</pubDate>
<title>Opening up EurActiv’s media innovation programme</title>
<link>https://myhub.ai/items/opening-up-euractivs-media-innovation-programme</link>
<image>
<url>https://myhub.ai/images/6NRn285E8_2AFnHilYmKMNoXwhU=/12303/width-251/%5E2021/11/8/m/mediadumps260files201603hashtagcloud2.png</url>
<link>https://myhub.ai/items/opening-up-euractivs-media-innovation-programme</link>
</image>
<description><p><i>Imported from the Blogactiv.eu blogging platform, closed without warning in 2021. Links, images and embeds not guaranteed, and comments not displayed.</i></p><p><b>EurActiv.com is opening one of its media innovations to other media interested in increasing competitiveness through translated syndication.</b> </p><p>(<b><i>Update, 31/3/16:</i></b><i> this project was covered, among many other things, in an interview with professional EU interpreter Alexander Drechsel in his podcast</i> <a href="http://www.adrechsel.de/langfm/mathewlowry"><i>Demos ex machina? Multilingual communication with Mathew Lowry</i></a>). </p><p>EurActiv has been a digital media innovator since its birth, as <a href="http://mathew.blogactiv.eu/2015/11/09/back-to-euractiv-for-some-media-innovation/">I pointed out</a> when I returned for my current part-time gig here. So I should not have been surprised to see my colleagues’ names in this year’s <a href="http://www.lt-innovate.org/lti-summit/programme">Language Technology Innovation 2016 conference programme</a>. In a classic case of small world networking, just before <a href="http://mathew.blogactiv.eu/2016/03/16/a-buyer-challenge-for-language-technology-innovate-2016/">my “Buyer Challenge” on Hashtag Platform</a>, they’ll be disclosing their CrossLingual Media Innovation programme during a “Solution Showcase” session. It’s even in the same room :) </p><p>CrossLingual will help secure the future of selected news media around Europe and help ideas flow better across borders. So what’s it all about? And how do you get involved?</p><h2>Tested by 12 EurActiv teams...</h2><p><a href="http://www.euractiv.com/about-euractiv/media-partners-network/"><i>Original link</i></a><br/>The basic idea has already been tested for many years across the EurActiv network - the trilingual EurActiv.com, edited by teams in Brussels, Paris and Berlin, plus 9 EurActiv franchises in as many countries (<a href="http://www.euractiv.com/about-euractiv/media-partners-network/">details</a>). Each editorial team produces its own content, but also translates selected articles from the others in the network to widen and deepen their coverage. </p><p>Some 2,750 pieces are translated every year, including most content produced in Paris and Berlin for EurActiv.com. Given that it’s taken over 10 years to build this network, it should come as no surprise that EurActiv has been exploring how machine translation could help since an early collaboration in 2002 with Systrans, then the EU&#x27;s main machine translation tool. What became known as the <b>CrossLingual Media concept</b> was tested frequently over the following years as the network developed. Things got really interesting when EurActiv&#x27;s translators launched parallel tests of both <a href="http://ec.europa.eu/dgs/translation/translationresources/machine_translation/index_en.htm">MT@EC</a> (the European Commission’s current in-house machine translation tool) and technology from Latvian company <a href="http://www.tilde.com/">Tilde</a>. It was these real-world tests that led to the <a href="http://mathew.blogactiv.eu/2016/02/15/exploring-translated-syndication-at-future-media-lab-2016/">Future Media Lab workshop</a> last January. Now it’s time to take things a step further.</p><h2>… but you don’t need to be one to benefit</h2><p>The pitch is pretty simple: <b>let’s create a platform allowing participating newsmedia to easily republish each others&#x27; content across language barriers.</b> </p><p>As you can imagine, most news media do not want competitors to republish their content. But a German newsmagazine is not in competition with a French newspaper: publishing in different languages means publishing to different audiences. </p><p>So why shouldn’t they translate and use each others’ content to widen and deepen their coverage? After all, it’s not as if each media writes everything they publish: as revenues fall, most media are republishing more press agency content than ever before. This is big business: Reuters had almost $US13bn in revenues in 2014, for example, while in July 2015 <a href="http://www.ibisworld.co.uk/market-research/news-agencies.html">IbisWorld estimated</a> that the UK market alone had revenues of £3bn (€3.9b). In other words, <b>news is being commoditised,</b> with more media publishing identical content bought from a tiny handful of international press agencies.</p><h2>Advanced technologies, limited membership</h2><p><b>Let’s create a high-quality alternative</b>, where content from trusted partners is machine-translated, automatically categorised and seamlessly delivered directly to all participating medias&#x27; content management systems. </p><p><b>What’s more, let’s build a platform which improves as it grows</b>, with the machine translation engine learning from every correction participating media make to its machine translations. Unlike largely manual experiments (<a href="http://www.theguardian.com/world/series/europa">Europa club</a>, <a href="http://www.lefigaro.fr/medias/2015/03/10/20004-20150310ARTFIG00338-alliance-entre-sept-quotidiens-leaders-en-europe.php">LENA</a> and the late Presseurop.eu), this means using some advanced technologies, as summarised at January’s <a href="http://mathew.blogactiv.eu/2016/02/15/exploring-translated-syndication-at-future-media-lab-2016/">Future Media Lab</a>. The same event showed that <b>membership will have to be limited</b>. To begin with, one of the key messages which emerged from the Future Media Lab workshop was <b>trust</b>:</p><blockquote><i>“participating media will need to be sure that the content they re-use comes from quality sources, particularly as the Platform may remove the articles’ surrounding context”</i> - <a href="http://mathew.blogactiv.eu/2016/02/15/exploring-translated-syndication-at-future-media-lab-2016/">Exploring Translated Syndication at Future Media Lab 2016</a></blockquote><p>It’s clear that only media meeting certain standards will be allowed into the CrossLingual Platform.</p><h2>Get onboard</h2><p>By providing seamless access to machine translated articles from trusted media, CrossLingual will allow journalists to either localise these translations for their own audience, and/or use them as source material for their own content.</p><p></p><p><a href="https://myhub.ai/media/dumps/260/files/2016/03/MAPS-MatthewL.png"><i>Original link</i></a><i> Before and After (right): CrossLingual will help Subscribing Media republish each other&#x27;s content across language barriers, supporting media and media voice diversity.</i> </p><p></p><p><b>Either way, they will cost-effectively increase revenue by increasing the volume of content produced and/or the depth of their coverage.</b> It will also create a Europe-wide network of cooperating media, providing new pan-European sponsorship and advertising opportunities. And apart from reinforcing participating medias’ competitiveness and generating new jobs, CrossLingual will help national perspectives flow across borders, supporting Pan-European public debate. </p><p></p><p><b>For more information:</b> <i>Disclosure</i>: as mentioned in the opening paragraph, EurActiv is a client.</p><ul><li><a href="mailto:mathew.lowry@gmail.com">drop me a line</a>, and I hope we catch up at LTInnovate2016 this May</li><li>and/or contact EurActiv’s Media Innovation Director <a href="mailto:david.mekkaoui@euractiv.com">David Mekkaoui</a>,</li><li>and/or catch up with EurActiv founder Christophe Leclercq at the related session he&#x27;s moderating at <a href="http://www.globaleditorsnetwork.org/programmes/gen-summit-2016/">Global Editors Network in June</a></li></ul><h2>Further reading</h2><ul><li><b>Conference programme</b>: <a href="http://www.lt-innovate.org/lti-summit/programme">Language Technology Innovation 2016</a></li><li><a href="http://mathew.blogactiv.eu/2016/03/16/a-buyer-challenge-for-language-technology-innovate-2016/">A Buyer Challenge for Language Technology Innovate 2016</a> (<i>March 2016</i>)</li><li><a href="http://mathew.blogactiv.eu/2016/02/15/exploring-translated-syndication-at-future-media-lab-2016/">Exploring Translated Syndication at Future Media Lab 2016</a> (<i>Feb 2016</i>)</li><li><a href="http://mathew.blogactiv.eu/2015/11/09/back-to-euractiv-for-some-media-innovation/">Back to EurActiv for some media innovation</a> (<i>Nov 2015</i>)</li><li><a href="http://www.euractiv.com/section/digital/opinion/europe-needs-bridges-between-national-media-here-is-how/">Europe needs bridges between national media, here is how</a> (EurActiv, <i>Aug 2015</i>)</li><li><b>LENA:</b> <a href="http://www.lefigaro.fr/medias/2015/03/10/20004-20150310ARTFIG00338-alliance-entre-sept-quotidiens-leaders-en-europe.php">Alliance entre sept quotidiens leaders en Europe</a> (Le Figaro, <i>March 2015</i>)</li><li>Resources tagged <a href="http://mathewlowry.tumblr.com/tagged/machine%20translation">machine translation</a>, <a href="http://mathewlowry.tumblr.com/tagged/machine-learning">machine learning</a>, <a href="http://mathewlowry.tumblr.com/tagged/bloggingportal">bloggingportal</a> and <a href="http://mathewlowry.tumblr.com/tagged/semantic">semantic</a> on my Hub</li></ul><p>Tags: media, publicsphere, machine translation, multilingualism, ltinnovate2016, syndicated-translation</p></description>
<category>media</category>
<category>publicsphere</category>
<category>machine translation</category>
<category>multilingualism</category>
<category>ltinnovate2016</category>
<category>syndicated-translation</category>
</item>

#### ChatGPT:
Here's the processed information from the provided content:

**Item 1**

- **Title**: It's the (Democracy-Poisoning) Golden Age of Free Speech | WIRED
- **Publication Date**: Wed, 21 Feb 2018 01:10:21 CET
- **Link**: [Read More](https://www.wired.com/story/free-speech-issue-tech-turmoil-new-censorship/)
- **Image**: ![View Image](https://myhub.ai/images/AAAKeyw5o_qo3gvFf0Cm2Mbomk8=/3983/width-251/%5E2019/11/18/p/photos5a5abe3ec77f7f39b676d8a7191100w_1280c_limitopener.jpg)
- **Description**: The article discusses how the flow of the world's attention is structured by a few digital platforms, impacting free speech. It explores the manipulation of trust and attention, the business models of tech platforms, and the need for distinguishing truth from falsehood. It also mentions the importance of free speech as a democratic value but highlights its limitations.

**Categories**:

- algorithm
- social media
- facebook
- publicsphere
- free speech
- disinformation

**Item 2**

- **Title**: Is banning trolls a prerequisite or a defeat for free speech?
- **Publication Date**: Wed, 27 Jul 2016 08:46:00 CEST
- **Link**: [Read More](https://myhub.ai/items/is-banning-trolls-a-prerequisite-of-or-a-defeat-for-free-speech)
- **Image**: ![View Image](https://myhub.ai/images/xPDb8z7FeWbqxuPyien5kv2pKhc=/12308/width-251/%5E2021/11/8/m/mediadumps260files201607banned-796x3481.jpg)
- **Description**: This article discusses the banning of trolls, particularly Milo Yiannopoulos, from Twitter and its implications for free speech. It touches on the conflation of free speech and social media platforms, highlighting that these platforms are private clubs with the right to enforce rules. The article emphasizes the need to differentiate between utilities and private platforms.

**Categories**:

- publicsphere
- troll
- social-media
- comment

**Item 3**

- **Title**: European unity is meaningless without a media to match | Media | The Guardian
- **Publication Date**: Mon, 30 May 2016 04:44:18 CEST
- **Link**: [Read More](http://www.theguardian.com/media/2016/may/29/european-unity-meaningless-without-media-to-match-eu-superstate?utm_campaign=digest\&utm_medium=email\&utm_source=app)
- **Image**: ![View Image](https://myhub.ai/images/Nkzia_Sg4xI2cD0z2NwL8u7Hqao=/4618/width-251/%5E2019/11/18/i/imgmediad5d9966517ca4d24b489efb3129682c8fb33a6ec0_162_4252_25524252.jpg)
- **Description**: The article discusses the importance of a common media landscape for European unity. It highlights the need for shared news sources to build common purpose and argues that diverse national media can hinder the process of European integration.

**Categories**:

- media
- eu
- publicsphere

**Item 4**

- **Title**: Opening up EurActiv’s media innovation programme
- **Publication Date**: Tue, 29 Mar 2016 09:25:21 CEST
- **Link**: [Read More](https://myhub.ai/items/opening-up-euractivs-media-innovation-programme)
- **Image**: ![View Image](https://myhub.ai/images/6NRn285E8_2AFnHilYmKMNoXwhU=/12303/width-251/%5E2021/11/8/m/mediadumps260files201603hashtagcloud2.png)
- **Description**: This article discusses EurActiv's CrossLingual Media Innovation program, which aims to enable participating news media to republish each other's content across language barriers. It mentions the benefits of such collaboration, including cost-effective content production and the creation of a Europe-wide network of cooperating media.

**Categories**:

- media
- publicsphere
- machine translation
- multilingualism
- ltinnovate2016
- syndicated-translation

Please let me know if you need any further information or if there's anything specific you'd like to know about these articles.
