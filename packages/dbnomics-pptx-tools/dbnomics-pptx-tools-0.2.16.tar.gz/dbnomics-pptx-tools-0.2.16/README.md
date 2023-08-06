# DBnomics PowerPoint (pptx) tools

This CLI tool allows to update data coming from DBnomics in PowerPoint presentations.

## Usage

First, define a YAML metadata file describing the charts and tables on each slide to update.

For example see [simple_presentation_1.yaml](./samples/simple_presentation_1.yaml).

See the [metadata file](#metadata-file) section below for more details.

The `dbnomics-pptx` CLI command provides 2 commands: `fetch` and `update`.

### `fetch` command

This command reads all the series needed by the charts and tables of all slides in the YAML metadata file, deduplicate and download them in a cache directory, where they are stored as JSON files.

```bash
dbnomics-pptx fetch samples/simple_presentation_1.yaml
```

Use the `-v` option to display debug messages.

By default, the series that are already present in the cache directory are skipped, in order to avoid putting pressure on DBnomics servers.
Use the `--force` option to always download them.

### `update` command

This command takes a PowerPoint presentation file in input, and a YAML metadata file, and updates the charts and tables defined in the metadata file, then saves the result in an output presentation file (it does not modify the input one).

```bash
dbnomics-pptx update samples/simple_presentation_1.pptx --metadata-file samples/simple_presentation_1.yaml samples/simple_presentation_1.output.pptx
```

Use the `-v` option to display debug messages.

## Metadata file

```yaml
slides:
  My slide 1: # the title of the slide
    charts:
      My chart 1: # the name of the chart (as defined in the "Selection pane")
        series:
          - OECD/GDP_GROWTH/W.USA.tracker_yoy # simple form: the series ID
          - id: OECD/GDP_GROWTH/W.Eurozone.tracker_yoy # extended form: a map of the ID and the name of the series
            name: Eurozone
    tables:
      My table 1: # the name of the table (as defined in the "Selection pane")
        series:
          - OECD/KEI/NAEXKP01.EA19.GP.A
          - OECD/KEI/NAEXKP01.DEU.GP.A
          - OECD/KEI/NAEXKP01.FRA.GP.A
          - OECD/KEI/NAEXKP01.ITA.GP.A
series: # a map of properties for series, shared between all the charts and tables of all slides
  OECD/GDP_GROWTH/W.USA.tracker_yoy:
    name: United States
  OECD/KEI/NAEXKP01.DEU.GP.A:
    name: Germany
  OECD/KEI/NAEXKP01.EA19.GP.A:
    name: Euro Area
  OECD/KEI/NAEXKP01.FRA.GP.A:
    name: France
  OECD/KEI/NAEXKP01.ITA.GP.A:
    name: Italy
```

Series properties defined in charts of tables have a higher precedence level than the ones defines in the top-level `series` map (which act as a fallback).

For example, here the name of the series `OECD/GDP_GROWTH/W.Eurozone.tracker_yoy` is defined at the chart level, in "My chart 1" (the name is "Eurozone"), and it is not defined in the top-level `series` map.
On the contrary, in "My chart 1", the named of the series `OECD/GDP_GROWTH/W.USA.tracker_yoy` is not defined, and will be found in the top-level `series` map, where it is defined as "United States".

### How to know the names of the charts/tables?

The names of the charts and tables can be read or modified in the "Selection pane" in PowerPoint.

The "Selection pane" can be opened with Alt+F10 in PowerPoint.
Then you just have to select a chart or a table, and it will highlight the corresponding line in the "Selection pane", showing its name.

You can also modify the name to improve readability.

Once you get the name of a chart or a table, you can put it in the YAML file.
In the previous example, the names are "My chart 1" and "My table 1".

See also:

- [Manage objects with the Selection pane](https://support.microsoft.com/en-us/office/manage-objects-with-the-selection-pane-a6b2fd3e-d769-46c1-9b9c-b94e04a72550)
- [The PowerPoint Selection Pane](https://www.presentationpoint.com/blog/powerpoint-selection-pane/)
