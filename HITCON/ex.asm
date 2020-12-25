   0:   c3                      ret    
   1:   a8 c3                   test   al, 0xc3
   3:   bf c3 bf c3 bf          mov    edi, 0xbfc3bfc3
   8:   c3                      ret    
   9:   bf c3 80 5f c2          mov    edi, 0xc25f80c3
   e:   b9 c2 b8 03 01          mov    ecx, 0x103b8c2
  13:   01 c2                   add    edx, eax
  15:   81 c3 b1 01 01 01       add    ebx, 0x10101b1
  1b:   01 c2                   add    edx, eax
  1d:   83 c3 87                add    ebx, 0xffffff87
  20:   1d 33 c3 b6 c3          sbb    eax, 0xc3b6c333
  25:   bc c2 8a 07 3c          mov    esp, 0x3c078ac2
  2a:   05 0f 44 c3 86          add    eax, 0x86c3440f
  2f:   c2 aa c3                ret    0xc3aa
  32:   a2 c3 b6 c3 a8          mov    ds:0xa8c3b6c3, al
  37:   05 05 05 05 5e          add    eax, 0x5e050505
  3c:   c2 8b c3                ret    0xc38b
  3f:   be c2 81 c3 86          mov    esi, 0x86c381c2
  44:   c2 8b 02                ret    0x28b
  47:   05 05 c2 b9 03          add    eax, 0x3b9c205
  4c:   05 05 05 c3 bc          add    eax, 0xbcc30505
  51:   c2 ad 01                ret    0x1ad
  54:   3c 07                   cmp    al, 0x7
  56:   c3                      ret    
  57:   a2 c3 ba 55 c2          mov    ds:0xc255bac3, al
  5c:   8b c3                   mov    eax, ebx
  5e:   ac                      lods   al, BYTE PTR ds:[esi]
  5f:   c2 83 c3                ret    0xc383
  62:   a4                      movs   BYTE PTR es:[edi], BYTE PTR ds:[esi]
  63:   c3                      ret    
  64:   b8 c2 81 c3 ac          mov    eax, 0xacc381c2
  69:   24 02                   and    al, 0x2
  6b:   05 05 53 56 57          add    eax, 0x57565305
  70:   c2 b9 c2                ret    0xc2b9
  73:   8d 10                   lea    edx, [eax]
  75:   c2 b7 c3                ret    0xc3b7
  78:   b8 c3 a8 c2 b3          mov    eax, 0xb3c2a8c3
  7d:   01 05 05 68 c2 97       add    DWORD PTR ds:0x97c26805, eax
  83:   02 05 05 c3 bf c3       add    al, BYTE PTR ds:0xc3bfc305
  89:   90                      nop
  8a:   c2 b9 40                ret    0x40b9
  8d:   c3                      ret    
  8e:   95                      xchg   ebp, eax
  8f:   c3                      ret    
  90:   9c                      pushf  
  91:   2d c3 a8 c2 a2          sub    eax, 0xa2c2a8c3
  96:   01 05 05 c2 b9 6f       add    DWORD PTR ds:0x6fb9c205,  eax
  9c:   c3                      ret    
  9d:   b1 c3                   mov    cl, 0xc3
  9f:   94                      xchg   esp, eax
  a0:   c2 9f c2                ret    0xc29f
  a3:   8b c3                   mov    eax, ebx
  a5:   b0 c3                   mov    al, 0xc3
  a7:   a8 c2                   test   al, 0xc2
  a9:   96                      xchg   esi, eax
  aa:   01 05 05 c2 b9 c2       add    DWORD PTR ds:0xc2b9c205, eax
  b0:   82 c2 a1                add    dl, 0xa1
  b3:   0d c2 a5 c2 8b          or     eax, 0x8bc2a5c2
  b8:   c3                      ret    
  b9:   b8 c3 a8 c2 8a          mov    eax, 0x8ac2a8c3
  be:   01 05 05 c2 b9 70       add    DWORD PTR ds:0x70b9c205, eax
  c4:   c2 be 1c                ret    0x1cbe
  c7:   23 c2                   and    eax, edx
  c9:   89 44 24 1c             mov    DWORD PTR [esp+0x1c], eax
  cd:   c3                      ret    
  ce:   a8 7c                   test   al, 0x7c
  d0:   01 05 05 c2 b9 c3       add    DWORD PTR ds:0xc3b9c205, eax
  d6:   91                      xchg   ecx, eax
  d7:   c3                      ret    
  d8:   be 73 1b c2 89          mov    esi, 0x89c21b73
  dd:   44                      inc    esp
  de:   24 20                   and    al, 0x20
  e0:   c3                      ret    
  e1:   a8 6e                   test   al, 0x6e
  e3:   01 05 05 c2 b9 c3       add    DWORD PTR ds:0xc3b9c205, eax
  e9:   a2 c3 ba 1b 01          mov    ds:0x11bbac3, al
  ee:   c3                      ret    
  ef:   a8 64                   test   al, 0x64
  f1:   01 05 05 c2 b9 c3       add    DWORD PTR ds:0xc3b9c205, eax
  f7:   89 53 29                mov    DWORD PTR [ebx+0x29], edx
  fa:   c3                      ret    
  fb:   9c                      pushf  
  fc:   c2 89 44                ret    0x4489
  ff:   24 18                   and    al, 0x18
 101:   c3                      ret    
 102:   a8 56                   test   al, 0x56
 104:   01 05 05 c2 b9 6e       add    DWORD PTR ds:0x6eb9c205, eax
 10a:   c2 85 1c                ret    0x1c85
 10d:   5c                      pop    esp
 10e:   c2 89 44                ret    0x4489
 111:   24 0c                   and    al, 0xc
 113:   c3                      ret    
 114:   a8 48                   test   al, 0x48
 116:   01 05 05 c2 b9 c3       add    DWORD PTR ds:0xc3b9c205, eax
 11c:   a0 53 31 4b c2          mov    al, ds:0xc24b3153
 121:   89 44 24 14             mov    DWORD PTR [esp+0x14], eax
 125:   c3                      ret    
 126:   a8 3a                   test   al, 0x3a
 128:   01 05 05 c2 b9 c2       add    DWORD PTR ds:0xc2b9c205, eax
 12e:   98                      cwde   
 12f:   c2 94 c2                ret    0xc294
 132:   8e c3                   mov    es, ebx
 134:   8a c2                   mov    al, dl
 136:   8b c3                   mov    eax, ebx
 138:   98                      cwde   
 139:   c3                      ret    
 13a:   a8 2e                   test   al, 0x2e
 13c:   01 05 05 c2 89 44       add    DWORD PTR ds:0x4489c205, eax
 142:   24 24                   and    al, 0x24
 144:   c2 8d c2                ret    0xc28d
 147:   84 24 c2                test   BYTE PTR [edx+eax*8], ah
 14a:   a0 05 05 05 50          mov    al, ds:0x50050505
 14f:   68 02 02 05 05          push   0x5050202
 154:   c3                      ret    
 155:   bf c3 96 33 c3          mov    edi, 0xc33396c3
 15a:   89 c2                   mov    edx, eax
 15c:   85 c3                   test   ebx, eax
 15e:   80 0f c2                or     BYTE PTR [edi], 0xc2
 161:   85 c3                   test   ebx, eax
 163:   9a 05 05 05 51 51 51    call   0x5151:0x51050505
 16a:   6a 06                   push   0x6
 16c:   6a 01                   push   0x1
 16e:   6a 02                   push   0x2
 170:   58                      pop    eax
 171:   50                      push   eax
 172:   c3                      ret    
 173:   bf c3 97 c2 8b          mov    edi, 0x8bc297c3
 178:   c3                      ret    
 179:   b0 33                   mov    al, 0x33
 17b:   c3                      ret    
 17c:   bf c2 83 c3 be          mov    edi, 0xbec383c2
 181:   c3                      ret    
 182:   bf 0f c2 84 c3          mov    edi, 0xc384c20f
 187:   82 05 05 05 c2 8d 44    add    BYTE PTR ds:0x8dc20505, 0x44
 18e:   24 10                   and    al, 0x10
 190:   50                      push   eax
 191:   57                      push   edi
 192:   57                      push   edi
 193:   68 c2 aa 02 05          push   0x502aac2
 198:   05 c3 bf 54 24          add    eax, 0x2454bfc3
 19d:   1c c2                   sbb    al, 0xc2
 19f:   85 c3                   test   ebx, eax
 1a1:   80 0f c2                or     BYTE PTR [edi], 0xc2
 1a4:   85 c2                   test   edx, eax
 1a6:   aa                      stos   BYTE PTR es:[edi], al
 1a7:   05 05 05 6a 02          add    eax, 0x26a0505
 1ac:   57                      push   edi
 1ad:   57                      push   edi
 1ae:   6a 10                   push   0x10
 1b0:   c2 8d 44                ret    0x448d
 1b3:   24 48                   and    al, 0x48
 1b5:   50                      push   eax
 1b6:   c2 8b 44                ret    0x448b
 1b9:   24 24                   and    al, 0x24
 1bb:   c3                      ret    
 1bc:   bf 70 10 c3 bf          mov    edi, 0xbfc31070
 1c1:   70 18                   jo     0x1db
 1c3:   c3                      ret    
 1c4:   bf 54 24 30 6a          mov    edi, 0x6a302454
 1c9:   02 58 66                add    bl, BYTE PTR [eax+0x66]
 1cc:   c2 89 44                ret    0x4489
 1cf:   24 28                   and    al, 0x28
 1d1:   c2 b8 05                ret    0x5b8
 1d4:   7b 05                   jnp    0x1db
 1d6:   05 66 c2 89 44          add    eax, 0x4489c266
 1db:   24 2a                   and    al, 0x2a
 1dd:   c2 8d 44                ret    0x448d
 1e0:   24 38                   and    al, 0x38
 1e2:   50                      push   eax
 1e3:   c3                      ret    
 1e4:   bf 54 24 1c 57          mov    edi, 0x571c2454
 1e9:   57                      push   edi
 1ea:   57                      push   edi
 1eb:   57                      push   edi
 1ec:   c2 89 44                ret    0x4489
 1ef:   24 3c                   and    al, 0x3c
 1f1:   c2 8d 44                ret    0x448d
 1f4:   24 38                   and    al, 0x38
 1f6:   6a 10                   push   0x10
 1f8:   50                      push   eax
 1f9:   56                      push   esi
 1fa:   c3                      ret    
 1fb:   bf 54 24 38 c2          mov    edi, 0xc2382454
 200:   85 c3                   test   ebx, eax
 202:   80 75 5e 6a             xor    BYTE PTR [ebp+0x5e], 0x6a
 206:   44                      inc    esp
 207:   5f                      pop    edi
 208:   c2 8b c3                ret    0xc38b
 20b:   8f c2                   pop    edx
 20d:   8d 44 24 58             lea    eax, [esp+0x58]
 211:   33 c3                   xor    eax, ebx
 213:   92                      xchg   edx, eax
 214:   c2 88 10                ret    0x1088
 217:   40                      inc    eax
 218:   c2 83 c3                ret    0xc383
 21b:   a9 01 75 c3 b8          test   eax, 0xb8c37501
 220:   c2 8d 44                ret    0x448d
 223:   24 48                   and    al, 0x48
 225:   c2 89 7c                ret    0x7c89
 228:   24 58                   and    al, 0x58
 22a:   50                      push   eax
 22b:   c2 8d 44                ret    0x448d
 22e:   24 5c                   and    al, 0x5c
 230:   c3                      ret    
 231:   87 c2                   xchg   edx, eax
 233:   84 24 c2                test   BYTE PTR [edx+eax*8], ah
 236:   88 05 05 05 05 01       mov    BYTE PTR ds:0x1050505, al
 23c:   05 05 50 52 52          add    eax, 0x52525005
 241:   52                      push   edx
 242:   6a 01                   push   0x1
 244:   52                      push   edx
 245:   52                      push   edx
 246:   68 c2 a2 02 05          push   0x502a2c2
 24b:   05 52 c2 89 c2          add    eax, 0xc289c252
 250:   b4 24                   mov    ah, 0x24
 252:   c3                      ret    
 253:   80 05 05 05 c2 89 c2    add    BYTE PTR ds:0x89c20505, 0xc2
 25a:   b4 24                   mov    ah, 0x24
 25c:   c2 bc 05                ret    0x5bc
 25f:   05 05 c2 89 c2          add    eax, 0xc289c205
 264:   b4 24                   mov    ah, 0x24
 266:   c2 b8 05                ret    0x5b8
 269:   05 05 c3 bf 54          add    eax, 0x54bfc305
 26e:   24 48                   and    al, 0x48
 270:   6a c3                   push   0xffffffc3
 272:   bf c3 bf 74 24          mov    edi, 0x2474bfc3
 277:   4c                      dec    esp
 278:   c3                      ret    
 279:   bf 54 24 2c 33          mov    edi, 0x332c2454
 27e:   c3                      ret    
 27f:   bf 57 c3 bf c3          mov    edi, 0xc3bfc357
 284:   93                      xchg   ebx, eax
 285:   5f                      pop    edi
 286:   5e                      pop    esi
 287:   33 c3                   xor    eax, ebx
 289:   80 5b c2 8b             sbb    BYTE PTR [ebx-0x3e], 0x8b
 28d:   c3                      ret    
 28e:   a5                      movs   DWORD PTR es:[edi], DWORD PTR ds:[esi]
 28f:   5d                      pop    ebp
 290:   c3                      ret    
 291:   83 53 56 c2             adc    DWORD PTR [ebx+0x56], 0xffffffc2
 295:   8b c3                   mov    eax, ebx
 297:   b1 33                   mov    cl, 0x33
 299:   c3                      ret    
 29a:   92                      xchg   edx, eax
 29b:   c3                      ret    
 29c:   ab                      stos   DWORD PTR es:[edi], eax
 29d:   12 0f                   adc    cl, BYTE PTR [edi]
 29f:   c2 be c3                ret    0xc3be
 2a2:   8b c3                   mov    eax, ebx
 2a4:   81 c3 8a 0d c2 80       add    ebx, 0x80c20d8a
 2aa:   c3                      ret    
 2ab:   bb 61 c2 8d 41          mov    ebx, 0x418dc261
 2b0:   c3                      ret    
 2b1:   a0 0f 4c c3 81          mov    al, ds:0x81c34c0f
 2b6:   03 c3                   add    eax, ebx
 2b8:   90                      nop
 2b9:   46                      inc    esi
 2ba:   c2 8a 1e                ret    0x1e8a
 2bd:   c2 84 c3                ret    0xc384
 2c0:   9b                      fwait
 2c1:   75 c3                   jne    0x286
 2c3:   a8 5e                   test   al, 0x5e
 2c5:   c2 8b c3                ret    0xc38b
 2c8:   82 5b c3 83             sbb    BYTE PTR [ebx-0x3d], 0x83
 2cc:   c2 8d 41                ret    0x418d
 2cf:   c3                      ret    
 2d0:   b8 c3 83 55 c2          mov    eax, 0xc25583c3
 2d5:   8b c3                   mov    eax, ebx
 2d7:   ac                      lods   al, BYTE PTR ds:[esi]
 2d8:   c2 83 c3                ret    0xc383
 2db:   ac                      lods   al, BYTE PTR ds:[esi]
 2dc:   14 53                   adc    al, 0x53
 2de:   56                      push   esi
 2df:   57                      push   edi
 2e0:   c2 89 4d                ret    0x4d89
 2e3:   c3                      ret    
 2e4:   b4 64                   mov    ah, 0x64
 2e6:   c2 a1 30                ret    0x30a1
 2e9:   05 05 05 c2 89          add    eax, 0x89c20505
 2ee:   45                      inc    ebp
 2ef:   c3                      ret    
 2f0:   bc c2 8b 45 c3          mov    esp, 0xc3458bc2
 2f5:   bc c2 8b 40 0c          mov    esp, 0xc408bc2
 2fa:   c2 8b 40                ret    0x408b
 2fd:   14 c2                   adc    al, 0xc2
 2ff:   8b c3                   mov    eax, ebx
 301:   b8 c2 89 45 c3          mov    eax, 0xc34589c2
 306:   ac                      lods   al, BYTE PTR ds:[esi]
 307:   c2 8b c3                ret    0xc38b
 30a:   8f c3                   pop    ebx
 30c:   a8 c3                   test   al, 0xc3
 30e:   92                      xchg   edx, eax
 30f:   c3                      ret    
 310:   bf c3 bf c3 bf          mov    edi, 0xbfc3bfc3
 315:   c2 8b 3f                ret    0x3f8b
 318:   c2 8b 70                ret    0x708b
 31b:   18 c2                   sbb    dl, al
 31d:   85 c3                   test   ebx, eax
 31f:   b6 74                   mov    dh, 0x74
 321:   4f                      dec    edi
 322:   c2 8b 46                ret    0x468b
 325:   3c c2                   cmp    al, 0xc2
 327:   8b 5c 30 78             mov    ebx, DWORD PTR [eax+esi*1+0x78]
 32b:   c2 85 c3                ret    0xc385
 32e:   9b                      fwait
 32f:   74 44                   je     0x375
 331:   c2 8b 4c                ret    0x4c8b
 334:   33 0c 03                xor    ecx, DWORD PTR [ebx+eax*1]
 337:   c3                      ret    
 338:   8e c3                   mov    es, ebx
 33a:   a8 c2                   test   al, 0xc2
 33c:   8e c3                   mov    es, ebx
 33e:   bf c3 bf c3 bf          mov    edi, 0xbfc3bfc3
 343:   c2 8b 4c                ret    0x4c8b
 346:   33 20                   xor    esp, DWORD PTR [eax]
 348:   c2 89 45                ret    0x4589
 34b:   c3                      ret    
 34c:   b8 03 c3 8e 33          mov    eax, 0x338ec303
 351:   c3                      ret    
 352:   80 c2 89                add    dl, 0x89
 355:   4d                      dec    ebp
 356:   c3                      ret    
 357:   b0 c2                   mov    al, 0xc2
 359:   89 45 c3                mov    DWORD PTR [ebp-0x3d], eax
 35c:   bc 39 44 33 18          mov    esp, 0x18334439
 361:   76 22                   jbe    0x385
 363:   c2 8b 0c                ret    0xc8b
 366:   c2 81 03                ret    0x381
 369:   c3                      ret    
 36a:   8e c3                   mov    es, ebx
 36c:   a8 6d                   test   al, 0x6d
 36e:   c3                      ret    
 36f:   bf c3 bf c3 bf          mov    edi, 0xbfc3bfc3
 374:   03 45 c3                add    eax, DWORD PTR [ebp-0x3d]
 377:   b8 39 45 c3 b4          mov    eax, 0xb4c34539
 37c:   74 1c                   je     0x39a
 37e:   c2 8b 45                ret    0x458b
 381:   c3                      ret    
 382:   bc c2 8b 4d c3          mov    esp, 0xc34d8bc2
 387:   b0 40                   mov    al, 0x40
 389:   c2 89 45                ret    0x4589
 38c:   c3                      ret    
 38d:   bc 3b 44 33 18          mov    esp, 0x1833443b
 392:   72 c3                   jb     0x357
 394:   9e                      sahf   
 395:   3b 7d c3                cmp    edi, DWORD PTR [ebp-0x3d]
 398:   ac                      lods   al, BYTE PTR ds:[esi]
 399:   75 c2                   jne    0x35d
 39b:   9c                      pushf  
 39c:   33 c3                   xor    eax, ebx
 39e:   80 5f 5e 5b             sbb    BYTE PTR [edi+0x5e], 0x5b
 3a2:   c3                      ret    
 3a3:   89 c3                   mov    ebx, eax
 3a5:   83 c2 8b                add    edx, 0xffffff8b
 3a8:   4d                      dec    ebp
 3a9:   c3                      ret    
 3aa:   bc c2 8b 44 33          mov    esp, 0x33448bc2
 3af:   24 c2                   and    al, 0xc2
 3b1:   8d 04 48                lea    eax, [eax+ecx*2]
 3b4:   0f c2 b7 0c 30 c2 8b    cmpps  xmm6, XMMWORD PTR [edi-0x743dcff4], 0x44
 3bb:   44 
 3bc:   33 1c c2                xor    ebx, DWORD PTR [edx+eax*8]
 3bf:   8d 04 c2                lea    eax, [edx+eax*8]
 3c2:   88 c2                   mov    dl, al
 3c4:   8b 04 30                mov    eax, DWORD PTR [eax+esi*1]
 3c7:   03 c3                   add    eax, ebx
 3c9:   86 c3                   xchg   bl, al
 3cb:   ab                      stos   DWORD PTR es:[edi], eax
 3cc:   c3                      ret    
 3cd:   9f                      lahf   
 3ce:   2f                      das    
 3cf:   05 05 05 c3 b2          add    eax, 0xb2c30505
 3d4:   05 05 05 c2 82          add    eax, 0x82c20505
 3d9:   01 05 05 77 73 32       add    DWORD PTR ds:0x32737705, eax
 3df:   5f                      pop    edi
 3e0:   33 32                   xor    esi, DWORD PTR [edx]
 3e2:   2e 64 6c                cs fs ins BYTE PTR es:[edi], dx
 3e5:   6c                      ins    BYTE PTR es:[edi], dx
 3e6:   05 63 6d 64 2e          add    eax, 0x2e646d63
 3eb:   65 78 65                gs js  0x453
 3ee:   05 31 32 37 2e          add    eax, 0x2e373231
 3f3:   30 2e                   xor    BYTE PTR [esi], ch
 3f5:   30 2e                   xor    BYTE PTR [esi], ch
 3f7:   31                      .byte 0x31
 3f8:   05                      .byte 0x5