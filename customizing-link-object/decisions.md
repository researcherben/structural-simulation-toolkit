
# design decision 1: complexity of a single wire

Options:

A-link-B:

    ┌───────────────┐  link   ┌───────────────┐
    │ component A   p─────────p   component B │
    └───────────────┘         └───────────────┘


A-link-wire-link-B:

    ┌───────────────┐ link  ┌────────────────┐  link   ┌───────────────┐
    │ component A   p───────p component wire p─────────p   component B │
    └───────────────┘       └────────────────┘         └───────────────┘


A-subAwire-link-subBwire-B:

    ┌────────────────┐                                               ┌────────────────────┐
    │              ┌─┴────────────────────┐ link  ┌──────────────────┴───┐                │
    │  component A │ subcomponent wire A  p───────p  subcomponent wire B │   component B  │
    │              └─┬────────────────────┘       └──────────────────┬───┘                │
    └────────────────┘                                               └────────────────────┘


Example of this: a single-mode fiber optic cable, https://en.wikipedia.org/wiki/Fiber-optic_cable

How top pick which option is relevant:
1) identify potential use cases
2) decide how much future proofing to invest in at this time
3) evaluate what we are optimizing for.

Potential use cases:
* latency. This can be modeled by all three approaches.
* signal degradation, e.g. attenuation. This can be modeled by
  * A-link-wire-link-B
  * A-subAwire-link-subBwire-B

what we are optimizing for
* Model performance. (More components doesn't scale as well)
* realism
* ease of implementation

TODO: is there a memory difference between
A-link-wire-link-B and A-subAwire-link-subBwire-B ?

ASCII diagrams were created using https://asciiflow.com/

# design decision 2: a bundle of wires

A single link between two components is
A-link-B:

    ┌──────────────┐   link    ┌───────────────┐
    │ component A  p───────────p   component B │
    └──────────────┘           └───────────────┘

Those two components can be connected by multiple links:
A-Nlinks-B:

    ┌───────────────┐   link   ┌─────────────────┐
    │               p──────────p                 │
    │               │          │                 │
    │               │   link   │                 │
    │               p──────────p                 │
    │ component A   │          │   component B   │
    │               │   link   │                 │
    │               p──────────p                 │
    └───────────────┘          └─────────────────┘


If interaction among the links needs to be modeled,
that could be treated as the behavior of a bundle:
A-Nlinks-bundle-Nlinks-B:

    ┌───────────────┐   link   ┌────────────────────┐ link    ┌─────────────────┐
    │               p──────────p                    p─────────p                 │
    │               │          │                    │         │                 │
    │               │   link   │                    │ link    │                 │
    │               p──────────p  component bundle  ├─────────p                 │
    │  component A  │          │                    │         │   component B   │
    │               │   link   │                    │ link    │                 │
    │               p──────────p                    ├─────────p                 │
    └───────────────┘          └────────────────────┘         └─────────────────┘


Since the multiple links provide no insight,
collapse to a single link:
A-link-bundle-link-B:

    ┌───────────────┐   link   ┌────────────────────┐ link    ┌────────────────┐
    │  component A  p──────────p  component bundle  ├─────────p  component B   │
    └───────────────┘          └────────────────────┘         └─────────────────┘

or the behavior of the bundle could be modeled in subcomponents:
A-subAbundle-link-subBbundle-B:

    ┌────────────────┐                                                   ┌────────────────────┐
    │              ┌─┴──────────────────────┐ link  ┌────────────────────┴───┐                │
    │  component A │ subcomponent bundle A  p───────p  subcomponent bundle B │   component B  │
    │              └─┬──────────────────────┘       └────────────────────┬───┘                │
    └────────────────┘                                                   └────────────────────┘


Example of this: a cat5 cable, e.g., https://en.wikipedia.org/wiki/Category_5_cable
A cat5 cable is comprised of 8 copper wires as 4 twisted pairs.

How top pick which option is relevant:
1. identify potential use cases
2. decide how much future proofing to invest in at this time
3. evaluate what we are optimizing for.


Whether multiple links can be modeled as a single link depends on the use cases.
* if interference among the adjacent wires is to be modeled, then the options are
  * A-Nlinks-bundle-Nlinks-B
  * A-link-bundle-link-B
  * A-subAbundle-link-subBbundle-B


ASCII diagrams were created using https://asciiflow.com/
