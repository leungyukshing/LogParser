# Log Parser

**Author:** Yucheng Liang

## Intro

Log Parser is used to parse a log file (`.txt`) and export it to a graylog engine for later analysis.

## Installation

1. Make sure you have the Docker installed.

2. Use the `docker-compose.yml` file to download the images and run it by:

   ```bash
   $ docker-compose up -d
   ```

3. Then you can open a brower and visit `http://127.0.0.1:9000`. You are expected to see the main page of graylog.

4. Then follow [Graylog Installation](https://leungyukshing.cn/archives/Graylog-Installation.html) to create a input source.



## Export log file

Make sure the log is formatted and matched the pattern inside the `log_parser.py`. Then run:

```bash
$ python3 log_parser.py [log_file]
```

It will parses the log and exports them to the graylog cluster. Then you can see your log in the website.