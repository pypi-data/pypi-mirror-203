# gig

## Setup and Install

```
pip install gig-nuuuwan
```

## Release History

### 3.0.9   (CURRENT RELEASE)
* Fixed windows unittests

### 3.0.8
* Fixed missing dependencies BUG 
* Replaced fuzzywuzzy with RapidFuzz for string matching

### 3.0.7 
* refactoring (removed deprecated utils.cache)

### 3.0.6 
* refactoring, optimizations

### 3.0.5 
* perf: Speed-up Ent.geo
* feat: Added Ent.lnglat
* feat: Added Ent.short_name, Ent.acronym

### 3.0.4 
* Fixed filter_parent_id BUG in Ent.list_from_name_fuzzy

### 3.0.3 
* Geo support for Ents

### 3.0.2
* GIGTableRow.dict_p, that returns value as a ratio of total
* Renamed various load functions. #BREAKING_CHANGE

### 3.0.1 
* Fixed Missing gig.core BUG

### 3.0.0 
* Major overhall. #MAJOR #BREAKING_CHANGE
