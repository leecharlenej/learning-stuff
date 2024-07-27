# -------------------- Basics
#F5 to run entire script
#Highlight + F8 to run partial script.

# -------------------- Store as a variable
#Gather user input and store in a variable

$Input = Read-Host -Prompt " Please enter your name"
#Write-Host "Hello $Input, it's very nice to meet you $Input"

if ($Input -eq "Paul") {
    write-host "Hello Paul, I remember you"
} elseif ($Input -eq "Mary"){
    write-host "Hello Paul, I remember you :D"
} else {
    write-host "Sorry, $Input.. I do not know who you are"
}

# -------------------- Write-host: To appear on console.
switch($input){
    "Paul" {write-host "I remember Paul" | Out-File -FilePath "test.txt"}
    "Mary" {write-host "I remember Mary" | Out-File -FilePath "test.txt"}
    default {write-host "I don't remember you at all.." | Out-File -FilePath "test.txt"}
} 

# -------------------- Echo: For logging purposes.
switch($input){
    "Paul" {echo "I remember Paul" | Out-File -FilePath "test.txt"}
    "Mary" {echo "I remember Mary" | Out-File -FilePath "test.txt"}
    default {echo "I don't remember you at all.." | Out-File -FilePath "test.txt"}
} 

# -------------------- Create a text file.
# cd, dir, mkdir
#$input > test.txt

# -------------------- Function
function GetName() {
    $Input = Read-Host -Prompt " Please enter your name"
    switch($input){
    "Paul" {write-host "I remember Paul" | Out-File -FilePath "test.txt"}
   "Mary" {write-host "I remember Mary" | Out-File -FilePath "test.txt"}
    default {write-host "I don't remember you at all.." | Out-File -FilePath "test.txt"}
    }
    # Write-host $Input # For logging on console.
    echo $Input
}

# -------------------- For loops
for ($i = 1; $i -le 10; $i++) {
#lt: less than, le: less than equal
    #$i
    #sleep -Milliseconds 100
    #Write-Progress -Activity "Counting to 100" -Status "$i complete" -PercentComplete $i
    Write-Progress -Activity "Counting to 100" -Status "$i% complete ($i/100)" -PercentComplete $i
    Sleep -Milliseconds 250
}

# -------------------- Creating folders

$prefix = Read-Host -Prompt "What would you like your folder prefix to be?"
$count = Read-Host -Prompt "How many folders would you like to create?"

for ($i = 1; $i -le $count; $i++) {
    Write-Progress -Activity "Coutning to 100" -Status "$i% Complete ($i / $)" -PercentComplete $i
    mkdir -Path "$($prefix)$($i)"
}

# -------------------- CSV

$csv = Import-csv -Path "C:\test\NewUsers.csv"

$csv | ogv # To view CSV in a Window

foreach ($line in $csv) {
    Write-Host "Creating folders for $($line. 'First Name' ) $($line.'Email Address')"

    # Create folders for user
    for ($i = 1; $i -le 5; $i++) {
        mkdir -Path "S(Sline.'Last Name')_$i"
    }
}