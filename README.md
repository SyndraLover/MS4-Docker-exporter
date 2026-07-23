# MuseScore4 Exporter inside Docker

**This Repository is only meant for Artists and Humans who appreciate Art by Artists.** 
See [Declaration](Declaration.md) for more.

This repository enables you to export your compositions inside a Docker-Container which you may or may not version with Git. 
It takes a SHA256-Hash of every .mscz File in the import directory and only re-renders them to the export directory if changed. 

it does not recurse over the import directory!
if you have a folder structure like this:
```sh
/Music/Op.1/Adagio.mscz
/Music/Op.2/Presto.mscz
/Music/Op.2/Moderato.mscz
/Music/Op.3/Largo.mscz
```

Then it will render nothing if you specify /Music as the import folder.

- You can specify the Rendered Files via setting the enviroment vars. Currently only Python-Booleans are allowed; True or False
    - MS4_PDF=True
    - MS4_MP3=True
    - MS4_MXL=True

## Usage

To run MuseScore4 Exporter, use the following command:
- Run
    ```sh
    docker run -it --rm -v /dir/to/import:/app/import:ro -v /dir/to/export:/app/export -e MS4_PDF=True -e MS4_MP3=True -e MS4_MXL=True ghcr.io/syndralover/musescore4_exporter:latest
    ```
If you wish to render everything again. Delete MS4_Export.json in the export directory

## Known Issues
- export directories are created by root if they do not exists; You can pass user:group to the container which maps uid and gid. 
**BEWARE of permission Errors if files and/or directories don't exist**
    ```sh
    docker run --user uid:gid -it --rm -v /dir/to/import:/app/import:ro -v /dir/to/export:/app/export -e MS4_PDF=True -e MS4_MP3=True -e MS4_MXL=True ghcr.io/syndralover/musescore4_exporter:latest
    ```
## License
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)