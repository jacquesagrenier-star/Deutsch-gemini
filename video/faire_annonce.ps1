# Annonces de haut-parleur, avec les voix OneCore de Windows.
#
# POURQUOI PAS ELEVENLABS ICI
#   L'annonce passe au filtre telephone (420-3600 Hz), recoit une grande
#   reverberation de hall et se pose 20 dB sous le dialogue. Apres ce
#   traitement, une voix Windows gratuite est indiscernable d'une voix
#   neurale -- et les credits ElevenLabs servent a ce qui s'entend vraiment.
#
# ATTENTION : System.Speech (SAPI5) NE VOIT PAS ces voix. Il faut passer par
# SpObjectTokenCategory sur la cle Speech_OneCore, comme ci-dessous.
#
#   powershell -NoProfile -File video/faire_annonce.ps1

$sortie = Join-Path $PSScriptRoot "..\audio\ambiance"
New-Item -ItemType Directory -Force -Path $sortie | Out-Null

$textes = @(
  @{ fichier = "annonce-paris-de.wav"; voix = "Katja";
     texte = "Meine Damen und Herren, letzter Aufruf fur die Passagiere des Fluges L H vier null sechs nach Paris. Bitte begeben Sie sich zum Gate A funfzehn." },
  @{ fichier = "annonce-paris-en.wav"; voix = "Linda";
     texte = "Ladies and gentlemen, this is the final call for passengers on flight L H four zero six to Paris. Please proceed to gate A fifteen." }
)

$cat = New-Object -ComObject SAPI.SpObjectTokenCategory
$cat.SetId("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices", $false)
$jetons = @($cat.EnumerateTokens())

foreach ($t in $textes) {
  $jeton = $jetons | Where-Object { $_.GetDescription() -like "*$($t.voix)*" } | Select-Object -First 1
  if (-not $jeton) { Write-Output "  voix introuvable : $($t.voix)"; continue }

  $voix = New-Object -ComObject SAPI.SpVoice
  $voix.Voice = $jeton
  # Debit normal : une annonce lente survivrait trop bien au filtre et
  # redeviendrait comprehensible, ce qu'on ne veut pas.
  $voix.Rate = 0

  $flux = New-Object -ComObject SAPI.SpFileStream
  $chemin = Join-Path $sortie $t.fichier
  $flux.Open($chemin, 3, $false)
  $voix.AudioOutputStream = $flux
  $voix.Speak($t.texte) | Out-Null
  $flux.Close()
  Write-Output "  $($t.fichier)  ($($jeton.GetDescription()))"
}
