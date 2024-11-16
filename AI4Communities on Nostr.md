# AI4Communities on Nostra

As mentioned above, Bluesky and Nostr already offer some elements of the infrastructure required for this. 


**I’m less familiar with Nostr,** but I know that Jack Dorsey, its founder and the guy who launched Bluesky when he ran Twitter, definitely [believes in algorithmic choice](https://cointelegraph.com/magazine/algorithm-choice-can-fix-social-media-but-only-on-decentralized-platforms/). My introduction to Nostr came via one of my favourite thinkers in this space, Gordon Brander ([6 resources](https://myhub.ai/@mathewlowry/?tags=gordon+brander)), whose [Nature's many attempts to evolve a Nostr](https://substack.com/home/post/p-143032514)
walks you through the various architectures, concluding with the Nostr approach, of which he’s clearly a fan: “_You sign messages with your key, then post them to one or more relays. Other users follow one or more relays. When they get a message, they use your key to verify you sent it_”.

Currently it's not clear to me how this doesn't result in a splinternet: if two relays don't talk to each other then how do messages find other people not linked to your relay(s)? 

But what Brander's piece did convince me (for now) is that the federated services architecture underpinning the A**ctivityHub-powered Fediverse** has a fundamental flaw:  "Federated networks become oligopolies at scale", due to general forces seen everywhere: "airline routes, power grids, trains, banks, Bitcoin mining, protein interactions, ecological food webs, neural networks". It happened to email, and now it's happening with the Fediverse, where calls to defederate Threads (which was 10x the rest of the Fediverse when it arrived) were ineffective.