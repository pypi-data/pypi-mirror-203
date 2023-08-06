  #100= 7.                    ( for j.var in range[7, 10]:    )
L1000
  IF [#100 EQ 10.] GOTO 1002
  #[#100 + 300]= 12.          (     ptr[j] = 12               )
  GOTO 1000
L1002
  #100= 7.                    ( for j.var in range[7, 10]:    )
L1003
  IF [#100 EQ 10.] GOTO 1005
  #[#100 + 300]= #100         (     ptr[j] = j                )
  GOTO 1003
L1005
  #100= 2.                    ( for j.var in range[2, 7]:     )
L1006
  IF [#100 EQ 7.] GOTO 1008
                              (     ptr[j] = [j + 2] ** 2 + 17)
  #[#100 + 300]= POW[#100 + 2.,2.] + 17.
  GOTO 1006
L1008
