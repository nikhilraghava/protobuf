# protobuf

> Protocol Buffers 💾 in Python - using Google's data interchange format

Protocol buffering is similar to pickling in python but protocol buffering allows interoperability with other languages. In this repository I have buffered two numbers, `num_a` and `num_b` and added them by reading them from the buffer and displayed the sum onto the terminal.

You can download the pre-built binary from Google's release page [here](https://github.com/google/protobuf/releases). After downloading and extracting the files, create a directory called `protoc` in the `C:\Program Files` directory and move the extracted files over to the `protoc` directory. To compile `.proto` files in the future use the following command.

```bash
"C:\Program Files\protoc\bin\protoc" -I=SRC_DIR --python_out=DST_DIR PATH/TO/FILE.proto
```

In the above command, `SRC_DIR` is the source directory of your `.proto` file and `DST_DIR` is the destination directory of the generated python file that you wish to put the file into. The `PATH/TO/FILE.proto` is the path to your `.proto` file. To compile the `main.proto` file in this repository, type the following command.

```bash
"C:\Program Files\protoc\bin\protoc" -I=src --python_out=src src/main.proto
```