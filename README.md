# ja-quarkusio

Localization project for [quarkusio.github.io](https://github.com/quarkusio/quarkusio.github.io) (The repository for [quarkus.io website](https://quarkus.io))

Localized site: [https://ja-quarkusio.surge.sh/](https://ja-quarkusio.surge.sh)

## Translation workflow

Original [quarkusio.github.io](https://github.com/quarkusio/quarkusio.github.io) is built with Jekyll, and its contents are written in asciidoctor (.adoc) files.
ja-quarkusio extracts texts with [po4a](https://po4a.org/) utility, machine-translates with deepL, write back, and build a localized site.
Most workflow are automated by GitHub Actions except manual post-editing(translation).

### Prerequisites

All you need for your local environment is a CAT Tool like [POEdit](https://poedit.net/), which run on Win/Mac/Linux.

### Extracting texts from original repository

ja-quarkusio extracts texts with [po4a-updatepo](https://po4a.org/) utility from .adoc files to .adoc.po files, which saved in 
in [l10n/po](l10n/po) directory.
ja-quarkusio GitHub repository has a [GitHub Actions' periodic workflow](.github/workflows/sync-upstream.yml) to extract .adoc files stored in upstream submodule, 
which points [quarkusio.github.io](https://github.com/quarkusio/quarkusio.github.io) repository.

### Translating .po files

.po files need to be translated. .po file is a file format commonly used for software internationalization, and 
many software and SaaS can read/write.

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

## Contributing

Submitting a pull request, and reporting an issue are all welcome.

For translators, we have a [translation guide(ja)](./translation-guide.ja.md).

## License

ja-quarkusio is Open Source Project released under the
[Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html).
