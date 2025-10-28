dates=(
    "2024-11-14"
    "2023-11-24"
    "2024-03-14"
)

data_folder="./data"

csv_files=($(ls $data_folder/*.csv | sort))

if [ ${#csv_files[@]} -ne ${#dates[@]} ]; then
    echo "Number of CSV files and dates do not match!"
    exit 1
fi

for i in "${!csv_files[@]}"; do
    file="${csv_files[$i]}"
    date="${dates[$i]}"
    echo "=============================="
    echo "File: $file"
    echo "Date: $date"
    echo "Most active cookie(s):"
    python main.py -f "$file" -d "$date"
    echo "=============================="
    echo ""
done