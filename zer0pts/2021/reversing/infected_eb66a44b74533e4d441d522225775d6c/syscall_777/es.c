unsigned __int64 sub_7C0()
{
  char *v0; // rdi
  __int64 *v1; // rsi
  signed __int64 flagKeyIndex; // rcx
  __int16 v4; // [rsp+0h] [rbp-688h]
  char *v5; // [rsp+8h] [rbp-680h]
  char v6; // [rsp+10h] [rbp-678h]
  unsigned __int64 v7; // [rsp+678h] [rbp-10h]
 
  if ( prctl(38, 1LL, 0LL, 0LL, 0LL) )
    goto LABEL_10;

  v0 = &v6;
  flagKeyIndex = 410LL;
  v4 = 205;
  while ( flagKeyIndex )                                  // rep movs DWORD PTR es:[rdi], DWORD PTR ds:[rsi]
  {
    *v0 = *flagKey;
    flagKey = flagKey[4];
    v0 += 4;
    --flagKeyIndex;
  }
  v5 = &v6;
  
  if ( prctl(22, 2LL, &v4, *(_QWORD *)&v4, &v6) )
LABEL_10:
    exit(1);
}