<#
    Script that lists the content of a network drive, by specifing the path to the
    drive and also file extensions to be ignored. The ignored extensions will not
    be shown on the output, hence ignored.
    
    Written by xyz666
#>

$DrivePath = '\path\to\Drive'
$Extensions = [System.Collections.ArrayList]@('extensions','to','be','ignored')

function Search-Drive {
    
    param(
        [Parameter(Mandatory)]
        [string]$Path_to_OneDrive,

        [Parameter(Mandatory)]
        $Exclude_File_Type
    
    )

    Get-ChildItem -Path $Path_to_OneDrive -File -Recurse -Exclude $Exclude_File_Type
}

Search-Drive $DrivePath $Extensions