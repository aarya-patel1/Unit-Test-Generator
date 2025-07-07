mkdir build
cd build
cmake ..
cmake --build . | Out-File ../build_logs/build_output.txt -Encoding utf8
ctest --output-on-failure