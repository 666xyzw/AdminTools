<#
    The script is used to check remote drives or folders for files
    that should not be there. Ex.: your organization has a OneDrive
    set up for, lets say time sheets, and other than the time sheets
    there should not be anything else on the drive. This means 
    nothing besides: xls, xlsx, pdf or csv files. These files will
    be given to the script and it will omit them from the search,
    and will print out anything else.
    
    This script will attempt to run every time you open powerhsell.
    BUT first it will check 'Date.txt' file if the current date is
    there or not. If it isn`t then it means it did not run on the
    respective day, if the date is found in the file then the script
    exits.

    Usage:

    RunCheck \Path\to\the\Date.txt

    Inside the RunCheck function set Search-Drive \Path\to\Remote\Drive files_type_to_be_exclude_form_search

    Written by xyz666

#>

function Search-Drive {
    
    param(
        [Parameter(Mandatory)]
        [string]$Path_to_OneDrive,

        [Parameter(Mandatory)]
        $Exclude_File_Type
    
    )

    Get-ChildItem -Path $Path_to_OneDrive -File -Recurse -Exclude $Exclude_File_Type
}


function RunCheck {
    
    param(
    [Parameter(Mandatory)]
    [string]$Path_to_File
    )

    $Current_Date = Get-Date -Format "dd/MM/yyyy"
    $Data_from_File = Get-Content $Path_to_File

    Add-Content -Value $Current_Date -Path $Path_to_File
    if ($Data_from_File -ne $Current_Date) {
        
        Write-Host "Today I did not run!"
        Write-Host "Executing the Search-OneDrive script"

        Search-Drive '\path\to\remote\drive' file_extensions_to_exclude_from_search 

        $Current_Date | Out-File -Append -FilePath $Path_to_File
        
    }else{
        
        Write-Host "The Search-OneDrive script has run today already."
        Write-Host "Nothing to do!`r`n"
    }

}

RunCheck "\path\to\Date.txt"
