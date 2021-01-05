# i18n-quarkusio

Translation project for [quarkusio.github.io](https://github.com/quarkusio/quarkusio.github.io) (The repository for [quarkus.io website](https://quarkus.io))

Japanese: [https://ja-i18n-quarkusio.surge.sh/](https://ja-i18n-quarkusio.surge.sh)

## Translation workflow

Original [quarkusio.github.io](https://github.com/quarkusio/quarkusio.github.io) is built with Jekyll, and its contents are written in asciidoctor (.adoc) files.
i18n-quarkusio translates the site with [po4a](https://po4a.org/) utility.

### Prerequisites

* po4a
* ruby
* bundler

### Extracting texts from original repository

i18n-quarkusio extracts texts with [po4a-updatepo](https://po4a.org/) utility from .adoc files to .adoc.po files, which saved in 
in [i18n/po](i18n/po) directory.
i18n-quarkusio GitHub repository has a [GitHub Actions' periodic workflow](.github/workflows/sync-upstream.yml) to extract .adoc files stored in upstream submodule, 
which points [quarkusio.github.io](https://github.com/quarkusio/quarkusio.github.io) repository.

### Translating .po files

.po files need to be translated. .po file is a file format commonly used for software internationalization, and 
many software and SaaS can read/write. For example, [POEdit](https://poedit.net/), which run on Win/Mac/Linux, is a good candidate.

### Applying translated texts

Now you are ready to apply translated texts. With the command below, translated source tree are built in `translated` directory.

```
bin/apply-translation
```

### Build a translated site

You can build a translated site from `translated` directory with:

```
bin/exec-jekyll
```

## License

i18n-quarkusio is Open Source Project released under the
[Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html).
