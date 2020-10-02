VERSION 5.00
Begin VB.Form Form1 
   BackColor       =   &H00404000&
   BorderStyle     =   4  'Fixed ToolWindow
   Caption         =   "Transpose"
   ClientHeight    =   3000
   ClientLeft      =   45
   ClientTop       =   390
   ClientWidth     =   6600
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   3000
   ScaleWidth      =   6600
   ShowInTaskbar   =   0   'False
   StartUpPosition =   3  'Windows Default
   Begin VB.TextBox txtjumlahtrans 
      Height          =   375
      Left            =   5520
      TabIndex        =   3
      Text            =   "2"
      Top             =   360
      Width           =   855
   End
   Begin VB.TextBox txtsource 
      Height          =   495
      Left            =   2040
      MultiLine       =   -1  'True
      TabIndex        =   2
      Text            =   "Form1.frx":0000
      Top             =   240
      Width           =   3255
   End
   Begin VB.TextBox txthasil 
      Height          =   1695
      Left            =   2040
      MultiLine       =   -1  'True
      TabIndex        =   1
      Text            =   "Form1.frx":0013
      Top             =   840
      Width           =   3255
   End
   Begin VB.CommandButton Command1 
      Caption         =   "transpose"
      Height          =   495
      Left            =   120
      TabIndex        =   0
      Top             =   240
      Width           =   1815
   End
   Begin VB.Label Label2 
      BackStyle       =   0  'Transparent
      Caption         =   "Jumlah matriks"
      ForeColor       =   &H80000002&
      Height          =   375
      Left            =   5400
      TabIndex        =   5
      Top             =   120
      Width           =   1095
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "Raka Kuswanto @ decenzo Lab"
      ForeColor       =   &H80000002&
      Height          =   375
      Left            =   120
      TabIndex        =   4
      Top             =   2640
      Width           =   2775
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim matriks(1 To 10) As String
Private Sub Command1_Click()
For i = 1 To 10
matriks(i) = "" 'clear data matriks
Next
getTranspose txtsource, txtjumlahtrans.Text, txthasil
Me.Caption = Me.Caption + " " + txtjumlahtrans.Text + " Matriks"
End Sub
Public Function getTranspose(source As String, jumlahMatriks As Integer, hasilnya As TextBox)
On Error GoTo handle
Dim hasil As String
Dim kata As String
Dim jmlkata As Integer
Dim jmltrans As Integer
Dim count As Integer
count = 0
jmlkata = 0
kata = source
jmltrans = Val(jumlahMatriks)
For i = 1 To Len(kata)
     For j = 1 To jmltrans
        count = count + 1
        jmlkata = jmlkata + 1
        matriks(j) = matriks(j) & Mid(kata, count, 1)
     Next
   
   If jmlkata = jmltrans Then
   jmlkata = 0
   End If
   If count = Len(kata) Then
   Exit For
   End If
Next

hasilnya.Text = ""
For ii = 1 To 10
    If matriks(ii) <> "" Then
        hasilnya.Text = hasilnya.Text & matriks(ii) & "-"
        Else
        Exit Function
    End If
Next
handle:
Exit Function
End Function
