<#
    The script is used to check a remote drive for files that should
    not be there. Ex.: your organization has a network drive set up for,
    lets say time sheets, and other than the time sheet files there should
    not be anything else on the drive. This means nothing besides:
    xls, xlsx, pdf or csv files. These file extensions will be given
    to the script (in the $FileExtensions variable) and it will omit
    them from the search, and will print out anything else.
    
    This script will attempt to run every time you open powerhsell.
    BUT first it will check 'Date.txt' file if the current date is
    there or not. If it isn`t then it means it did not run on the
    respective day, if the date is found in the file then the script
    exits.

    Written by xyz666
#>

$DrivePath = '\path\to\drive'
$DatePath = '\path\to\Date.txt'
$FileExtensions = [System.Collections.ArrayList]@('extensions','to','be','ignored')

function Search-Drive {
    
    param(
        [Parameter(Mandatory)]
        [string]$Path_to_Drive,

        [Parameter(Mandatory)]
        $Exclude_File_Type
    
    )

    Get-ChildItem -Path $Path_to_Drive -File -Recurse -Exclude $Exclude_File_Type
}


function CheckDate {
    
    param(
    [Parameter(Mandatory)]
    [string]$Path_to_File
    )

    $Current_Date = Get-Date -Format "dd/MM/yyyy"
    $Data_from_File = Get-Content $Path_to_File
       
    if ($Data_from_File[-1] -ne $Current_Date) {
        
        Write-Host "Today I did not run!"
        Write-Host "Executing the Search-Drive script"

        Search-Drive $DrivePath $FileExtensions

        Add-Content -Path $Path_to_File -Value $Current_Date
        
    }else{
        
        Write-Host "The Search-Drive script has run today already."
        Write-Host "Nothing to do!`r`n"
    }
}

CheckDate $DatePath
