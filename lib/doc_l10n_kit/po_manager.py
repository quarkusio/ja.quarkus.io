import os
import subprocess
import glob
import shutil
import concurrent.futures
import json

class PoManager:

    __base_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

    __target_lang = "ja_JP"
    __excluded_yaml_files = []
    __html_files = []

    def __init__(self):
        __config_file_name = "{}/config/l10n-kit.json".format(self.__base_dir)
        with open(__config_file_name) as file:
            __config = json.load(file)
            self.__target_lang = __config["targetLang"]
            self.__excluded_yaml_files = __config["sourceSets"]["yaml"]["exclude"]
            self.__html_files = __config["sourceSets"]["html"]


    def update_po(self):
        self.update_adoc_po_files()
        self.update_md_po_files()
        self.update_yaml_po_files()
        self.update_html_po_files()

    def translate_po(self):
        self.mk_output_dir()
        self.translate_adoc_po_files()
        self.translate_md_po_files()
        self.translate_yaml_po_files()
        self.translate_html_po_files()

    def normalize(self):
        file_paths = glob.glob("l10n/po/**/*.po".format(self.__target_lang), recursive=True)
        file_paths = [ file_path for file_path in file_paths if os.path.isdir(file_path) == False ]
        print(file_paths)
        concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker").map(self.__normalize, file_paths)

    def __normalize(self, file_path):
        print("Processing: {}".format(file_path))
        subprocess.run("sed -e '/^#|/d' {} -i".format(file_path), shell=True, check=True)
        subprocess.run("msgcat --to-code=utf-8 --lang={} --no-wrap -o {} {}".format(self.__target_lang, file_path, file_path), shell=True, check=True)

    def update_adoc_po_files(self):
        items = glob.glob("upstream/**/*.adoc", recursive=True)
        relative_file_paths = [os.path.relpath(item, self.__base_dir + "/upstream") for item in items if os.path.isdir(item) == False]
        relative_file_paths = [ relative_file_path for relative_file_path in relative_file_paths]
        executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker")
        executor.map(self.__update_adoc_po_file, relative_file_paths)
        executor.shutdown(wait=True)

    def update_md_po_files(self):
        items = glob.glob("upstream/**/*.md", recursive=True)
        relative_file_paths = [os.path.relpath(item, self.__base_dir + "/upstream") for item in items if os.path.isdir(item) == False]
        relative_file_paths = [ relative_file_path for relative_file_path in relative_file_paths]
        executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker")
        executor.map(self.__update_md_po_file, relative_file_paths)
        executor.shutdown(wait=True)

    def update_yaml_po_files(self):
        items = glob.glob("upstream/**/*.yaml", recursive=True)
        relative_file_paths = [os.path.relpath(item, self.__base_dir + "/upstream") for item in items if os.path.isdir(item) == False]
        relative_file_paths = [relative_file_path for relative_file_path in relative_file_paths if ((relative_file_path in self.__excluded_yaml_files) == False)]
        executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker")
        executor.map(self.__update_yaml_po_file, relative_file_paths)
        executor.shutdown(wait=True)

    def update_html_po_files(self):
        relative_file_paths = self.__html_files
        relative_file_paths = [ relative_file_path for relative_file_path in relative_file_paths ]
        executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker")
        executor.map(self.__update_html_po_file, relative_file_paths)
        executor.shutdown(wait=True)

    def mk_output_dir(self):
        upstream = "{}/upstream".format(self.__base_dir)
        output_dir = "{}/translated/{}".format(self.__base_dir, self.__target_lang)
        shutil.rmtree(output_dir, ignore_errors=True)
        os.makedirs("{}/translated".format(self.__base_dir), exist_ok=True)
        shutil.copytree(upstream, output_dir)

    def translate_adoc_po_files(self):
        items = glob.glob("upstream/**/*.adoc", recursive=True)
        relative_file_paths = [os.path.relpath(item, self.__base_dir + "/upstream") for item in items if os.path.isdir(item) == False]
        relative_file_paths = [ relative_file_path for relative_file_path in relative_file_paths]
        executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker")
        executor.map(self.__translate_adoc_po_file, relative_file_paths)
        executor.shutdown(wait=True)

    def translate_md_po_files(self):
        items = glob.glob("upstream/**/*.md", recursive=True)
        relative_file_paths = [os.path.relpath(item, self.__base_dir + "/upstream") for item in items if os.path.isdir(item) == False]
        relative_file_paths = [ relative_file_path for relative_file_path in relative_file_paths]
        executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker")
        executor.map(self.__translate_md_po_files, relative_file_paths)
        executor.shutdown(wait=True)

    def translate_yaml_po_files(self):
        items = glob.glob("upstream/**/*.yaml", recursive=True)
        relative_file_paths = [os.path.relpath(item, self.__base_dir + "/upstream") for item in items if os.path.isdir(item) == False]
        relative_file_paths = [relative_file_path for relative_file_path in relative_file_paths if ((relative_file_path in self.__excluded_yaml_files) == False)]
        executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker")
        executor.map(self.__translate_yaml_po_file, relative_file_paths)
        executor.shutdown(wait=True)

    def translate_html_po_files(self):
        relative_file_paths = self.__html_files
        relative_file_paths = [ relative_file_path for relative_file_path in relative_file_paths]
        executor = concurrent.futures.ThreadPoolExecutor(thread_name_prefix="worker")
        executor.map(self.__translate_html_po_files, relative_file_paths)
        executor.shutdown(wait=True)


    def __update_adoc_po_file(self, relative_file_path):
        print("Processing: {}".format(relative_file_path))
        relative_file_dir = os.path.dirname(relative_file_path)
        os.makedirs("{}/l10n/po/{}/{}".format(self.__base_dir, self.__target_lang, relative_file_dir), exist_ok=True)
        subprocess.run("PERLLIB=vendor/po4a/lib vendor/po4a/po4a-updatepo --master-charset UTF-8 -f asciidoc -o tablecells --master upstream/{} --po l10n/po/{}/{}.po".format(relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)
        subprocess.run("msgcat --to-code=utf-8 --no-wrap -o l10n/po/{}/{}.po l10n/po/{}/{}.po".format(self.__target_lang, relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)

    def __update_md_po_file(self, relative_file_path):
        print("Processing: {}".format(relative_file_path))
        relative_file_dir = os.path.dirname(relative_file_path)
        os.makedirs("{}/l10n/po/{}/{}".format(self.__base_dir, self.__target_lang, relative_file_dir), exist_ok=True)
        subprocess.run("PERLLIB=vendor/po4a/lib vendor/po4a/po4a-updatepo --master-charset UTF-8 -f text -o markdown -o neverwrap --master upstream/{} --po l10n/po/{}/{}.po".format(relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)
        subprocess.run("msgcat --to-code=utf-8 --no-wrap -o l10n/po/{}/{}.po l10n/po/{}/{}.po".format(self.__target_lang, relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)

    def __update_yaml_po_file(self, relative_file_path):
        print("Processing: {}".format(relative_file_path))
        relative_file_dir = os.path.dirname(relative_file_path)
        os.makedirs("{}/l10n/po/{}/{}".format(self.__base_dir, self.__target_lang, relative_file_dir), exist_ok=True)
        subprocess.run("PERLLIB=vendor/po4a/lib vendor/po4a/po4a-updatepo --master-charset UTF-8 -f yaml --master upstream/{} --po l10n/po/{}/{}.po".format(relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)
        subprocess.run("msgcat --to-code=utf-8 --no-wrap -o l10n/po/{}/{}.po l10n/po/{}/{}.po".format(self.__target_lang, relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)

    def __update_html_po_file(self, relative_file_path):
        print("Processing: {}".format(relative_file_path))
        relative_file_dir = os.path.dirname(relative_file_path)
        os.makedirs("{}/l10n/po/{}/{}".format(self.__base_dir, self.__target_lang, relative_file_dir), exist_ok=True)
        subprocess.run("PERLLIB=vendor/po4a/lib vendor/po4a/po4a-updatepo --master-charset UTF-8 -f xhtml --master upstream/{} --po l10n/po/{}/{}.po".format(relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)
        subprocess.run("msgcat --to-code=utf-8 --no-wrap -o l10n/po/{}/{}.po l10n/po/{}/{}.po".format(self.__target_lang, relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)

    def __translate_adoc_po_file(self, relative_file_path):
        print("Processing: {}".format(relative_file_path))
        subprocess.run("PERLLIB=vendor/po4a/lib vendor/po4a/po4a-translate --master-charset UTF-8 --localized-charset UTF-8 -f asciidoc -o tablecells --keep 0 --master upstream/{} --localized translated/{}/{} --po l10n/po/{}/{}.po".format(relative_file_path, self.__target_lang, relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)

    def __translate_md_po_files(self, relative_file_path):
        print("Processing: {}".format(relative_file_path))
        subprocess.run("PERLLIB=vendor/po4a/lib vendor/po4a/po4a-translate --master-charset UTF-8 --localized-charset UTF-8 -f text -o markdown -o neverwrap --keep 0 --master upstream/{} --localized translated/{}/{} --po l10n/po/{}/{}.po".format(relative_file_path, self.__target_lang, relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)

    def __translate_yaml_po_file(self, relative_file_path):
        print("Processing: {}".format(relative_file_path))
        subprocess.run("PERLLIB=vendor/po4a/lib vendor/po4a/po4a-translate --master-charset UTF-8 --localized-charset UTF-8 -f yaml --keep 0 --master upstream/{} --localized translated/{}/{} --po l10n/po/{}/{}.po".format(relative_file_path, self.__target_lang, relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)

    def __translate_html_po_files(self, relative_file_path):
        print("Processing: {}".format(relative_file_path))
        subprocess.run("PERLLIB=vendor/po4a/lib vendor/po4a/po4a-translate --master-charset UTF-8 --localized-charset UTF-8 -f xhtml --keep 0 --master upstream/{} --localized translated/{}/{} --po l10n/po/{}/{}.po".format(relative_file_path, self.__target_lang, relative_file_path, self.__target_lang, relative_file_path), shell=True, check=True)
