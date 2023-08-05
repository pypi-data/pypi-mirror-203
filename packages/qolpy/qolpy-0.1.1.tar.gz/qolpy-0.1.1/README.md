<p align="center">
    <img src="https://drive.google.com/uc?id=1r9L_Kjdm1i4lCYOCq-bngr-yTl6OZ_lu" alt="py-qol logo" width="250" height="250" />
</p>

# qolpy v0.1.1

Are you tired of making the same module in every project? Not a problem! Qol has your back.

A suite of random but useful functions that are aimed at giving you "piece of cake" level comfortability. This is a python port of the [javascript quality of life](https://github.com/lewisjr/qol) and [javascript fstring](https://github.com/lewisjr/fstring) package

# Installation

    pip install qolpy

or

    pip3 install qolpy

# Importing

```python
# full import
import qolpy

# partial imports
from qolpy import random_colour, parse_date, num_parse, abbreviate, to_title_case, to_sentence_case
```

# Functions

## random_colour

Get a random colour; For those scenarios where you couldn't care less!

Returns a `string`

```python
c = random_colour()
c_rgb = random_colour("rgb")
c_cmyk = random_colour("cmyk")
c_hsv = random_colour("hsv")
c_hsl = random_colour("hsl")

print(c, c_rgb, c_cmyk, c_hsv, c_hsl);
# #f7f7f7, rgb(247,247,247), cmyk(0%,0%,0%,3%), hsv(0,0%,97%), hsl(0,0%,97%)
```

<details>
<summary><strong>Params</strong></summary>

| Parameter | Default Setting | Required? | Definition                                 | Options                            |
| --------- | --------------- | --------- | ------------------------------------------ | ---------------------------------- |
| setting   | `hex`           | No        | The type of colour you would like returned | `hex`, `rgb`, `cmyk`, `hsv`, `hsl` |

</details>
<br />

## parse_date

Send in date parameters and receive either an object with their metadata, or a parsed date (e.g `2 Sep 2020`); American formatting is possible (e.g `Sep 2 2020`).

Returns a `string` or `Date_Object`. You can spread the args and use kwargs such as below:

```python
import datetime

dt = datetime.datetime.now()
date_list = [dt.day, dt.weekday(), dt.month, dt.year]

pd = parse_date(*date_list, c_format="nll", american=True)
pd_full = parse_date(*date_list, c_format="lll")

print(pd, pd_full)
# April 15 2023, Saturday 15th April, 2023
```

<details>
<summary><strong>interface</strong></summary>

```python
	"day": {
		"short": str,
		"long": str,
		"ordinal_month": str,
		"ordinal_week": str,
		"week_number": int,
		"month_number": int
	},
	"month": {
		"short": str,
		"long": str,
		"ordinal": str,
		"number": int
	},
	"year": {
		"short": int,
		"long": int
	}
```

</details>
<br />

<details>
<summary><strong>Params</strong></summary>

| Parameter | Default Setting | Required? | Definition                                                    | Options                                                                                                       |
| --------- | --------------- | --------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| monthDay  | `none`          | Yes       | The day of the month                                          | type `number`                                                                                                 |
| weekDay   | `none`          | Yes       | The day of the week                                           | type `number`                                                                                                 |
| month     | `none`          | Yes       | The numeric month                                             | type `number`                                                                                                 |
| year      | `none`          | Yes       | The full numeric year                                         | type `number`                                                                                                 |
| format    | `none`          | No        | The date format you would like                                | n = numeric, s = shorthand text, l = full text; `nns`, `nnl`, `sss`, `ssl`, `lll`, `nss`, `nsl`, `nls`, `nll` |
| american  | `false`         | No        | Whether or not you would like the format to be 'Americanised' | `true`, `false`                                                                                               |

</details>
<br />

## num_parse

Convert a number into a string as if it's MS Excel!

Returns a `string`

```python
num = num_parse(2100.45)
num_europe = num_parse(2100.45, "punct")
num_custom = num_parse(2100.45, "-")

print(num, num_europe, num_custom)
# 2,100.45, 2.100,45, 2-100.45)
```

<details>
<summary><strong>Params</strong></summary>

| Parameter | Default Setting | Required? | Definition                       | Options                                                    |
| --------- | --------------- | --------- | -------------------------------- | ---------------------------------------------------------- |
| value     | `undefined`     | Yes       | The number you want to be parsed | `none`                                                     |
| setting   | `undefined`     | Yes       | The delimiter for the number     | `space`, `comma`, `punct`, any other delimiter as a string |

</details>
<br />

## abbreviate

```python
name = "lEwiS mOsho junior"

print(abbreviate(name))
# LMJ
```

Make an **abbreviation** of a string; Usually used for names. It returns an upper case abbreviation of the string.

<details>
<summary><strong>Params</strong></summary>

| Parameter | Default Setting | Required? | Definition                                                 |
| --------- | --------------- | --------- | ---------------------------------------------------------- |
| text      | `null`          | Yes       | The string you wish to abbreviate                          |
| delimiter | `" "`           | No        | The character or string that seperates words in the string |

</details>
<br />

## to_title_case

Make any string **title cased**. it returns a string in which every first letter of a word is upper cased with the rest being lower cased.

```python
const name = "lEwiS mOsho junior"

print(to_title_case(name))
# Lewis Mosho Junior
```

<details>
<summary><strong>Params</strong></summary>

| Parameter | Default Setting | Required? | Definition                                                 |
| --------- | --------------- | --------- | ---------------------------------------------------------- |
| text      | `null`          | Yes       | The string you wish to change to title case                |
| delimiter | `" "`           | No        | The character or string that seperates words in the string |

</details>
<br />

## to_sentence_case

Make any string **sentence cased**; The current sentence delimiters are:

- `.`
- `;`
- `:`
- `!`
- `?`

It returns a string in which every first letter of the first word of a sentence is capitalised, with the remainder of the senter being lower cased.

```python
sentence = "heLLo wOrLD, mY NAME is lEwis; i am a Developer."

print(to_sentence_case(sentence))
# Hello world, my name is lewis; I am a developer.
```

<details>
<summary><strong>Params</strong></summary>

| Parameter | Default Setting | Required? | Definition                                                 |
| --------- | --------------- | --------- | ---------------------------------------------------------- |
| txt       | `null`          | Yes       | The string you wish to change to sentence case             |
| delimiter | `" "`           | No        | The character or string that seperates words in the string |

</details>
<br />

# Changelog

## v0.1.x

<details open>
<summary><strong>v0.1.1</strong></summary>

- README completed
- `parse_date` error fixed
  - Used tp return `month` object when `nll` was specifically set as an arg for `c_format`
- Moved codebase into `src` folder

</details>

<details>
<summary><strong>v0.1.0</strong></summary>

- Initial release
- Excel number formatting, date parsing, random colour generation,string sentence casing, title casing, and abrreviations added and typed

</details>
