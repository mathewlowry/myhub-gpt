# Coopetition in the ATmosphere

**I'm interested in exploring how we can manage competition and cooperation in the atmosphere.**

> *Coopetition is a business strategy blending cooperation and competition, where rival companies collaborate for mutual benefit, such as developing new tech or expanding markets, while still competing fiercely in other areas like pricing or features, creating a paradoxical yet strategic interdependence.*

Possibly nobody else coming to Vancouver was actually fully grown in 1995, so you're going to have to take it from me: we are living through a 1995 moment in decentralised social computing. A new protocol-based information ecosystem has appeared, and people are being incredibly creative with it. 

How do we help all these innovators **cooperate** - thus growing the ATmosphere to the benefit of all - *and* **compete** - thus demonstrating its sustainability?

This is in fact already happening: 

* independent teams have built distinct apps using shared lexicons
* we're now seeing "stage 2" cooperation, where different teams, having built different lexicons for similar use cases, are now cooperating (eg standard.site). 

So what's next? Some intriguing questions include: 

* can teams create new apps by adopting, adapting and recombining lexicons and other open-source components developed by multiple teams, while maintaining credible exit?
* how can this cooperation be encouraged and supported to make the most of scarce resources?

## Recombining components: an example

For an example, take a look at what I want to do with my MyHub: combining components from multiple teams to create a user-friendly "onramp" platform for new users that nevertheless maintains credible exit:

![[myhub-atproto.png]]
*(from [[MyHub on the ATmosphere]])*

The above *"reading/thinking/writing/publishing stack"* can be built from multiple components, upon which various teams are already working for their own purposes:

| Component             | What It Does                                                                                                           | Also needed by | Their Focus                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------ |
| **Inbox**             | Present potentially interesting content to read and integrate into your personal library and/or public online presence | Sill           | Surfacing links from your social graph across multiple lexicons                |
| **Thinking Tool**     | Private notes, drafts, collaboration with friends                                                                      | NorthSky       | Private data with community boundaries                                         |
| **Publishing Engine** | Publish Hubs and other site types to web via PDS                                                                       | standard.site  | `site.standard.publication`, `site.standard.document`                          |
| **Groundmist**        | Local-first PDS integration                                                                                            | tbd            | push local files to PDS, providing credible exit from  the myhub thinking tool |

(This table is incomplete - I would hope to complete it in Vancouver.)

Note that credible exit it guaranteed *precisely* because it is built from open, shared components: myhub will compete through integrating them together in a user-friendly way, for the masses of users who have never visited GitHub or Tangled.

## Supporting cooperation

**I have developed a model which I would recommend funding organisations consider if they want to cost-effectively support the development of a portfolio of ATmosphere start-ups.** 

Briefly, the model **focuses funding on developing components useful to multiple start-ups** - the component required by Sill and MyHub, for example, would be prioritised because it serves (at least!) two startups. 

But components need not be limited to code: it could also include shared infrastructure. The obvious example is the CoCoMo content moderation service, relays and PDSs being developed by Eurosky in Europe. There may be many more, but - crucially - *only a conversation amongst startups can identify them.* 

In Vancouver, I'd like to explore this with the atproto.science community.
## Conclusion

It can be more complex for developers in different start-ups to cooperate together, so the default state is competition. 

This will probably not grow the ATmosphere as a whole. *Iff* startups wish to cooperate on underlying technologies like lexicons, supporting this collaboration will help grow the entire ecosystem. 

This model therefore has two results:

* Incredibly cost-effective: you literally support multiple start-ups with a single grant
* Build cooperation between startup teams, to mutual benefit.

As an added bonus, both results will grow the ATmosphere as a whole, which in turn will lift *all* startups.

