# ----------------------------------------------------------------------
# B2. PowerShell — diska vieta failā
# ----------------------------------------------------------------------

# Saglabā informāciju par brīvo vietu diskos CSV failā diski.csv, ko var atvērt Excel. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pirms saglabāšanas izvadi Write-Host rindu "Sākam eksportu".

$diski = Get-PSDrive -PSProvider FileSystem |
    Select-Object Name, Used, Free

# TODO: saglabā $diski failā diski.csv
$diski | Export-Csv -Path .\diski.csv -NoTypeInformation