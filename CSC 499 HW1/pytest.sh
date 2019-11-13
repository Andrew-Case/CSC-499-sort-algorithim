python sort.py "a"

diff --brief <(SortedFileAscd) <(Output) >/dev/null
comp_value=$?

if [ $comp_value -eq 1 ]
then
    echo "test 1 passed"
else
    echo "test 1 failed"
    exit 1

rm SortedFile.txt

python sort.py "d"

diff --brief <(SortedFileDesc) <(Output) >/dev/null
comp_value=$?

if [ $comp_value -eq 1 ]
then
    echo "test 2 passed"
else
    echo "test 2 failed"
    exit 1
fi
