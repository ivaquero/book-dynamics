#import "@local/qooklet:0.1.0": *
#import "@preview/subpar:0.2.2": grid as sgrid
#import "@preview/rexllent:0.3.3": xlsx-parser
#import "@preview/physica:0.9.5": *
#import "@preview/whalogen:0.3.0": ce

#let info = toml("info.toml").global

#let bib = bibliography("dynam.bib", style: "future-science")
