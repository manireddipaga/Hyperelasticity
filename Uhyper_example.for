      SUBROUTINE UHYPER(BI1,BI2,AJ,U,UI1,UI2,UI3,TEMP,NOEL,
     1 CMNAME,INCMPFLAG,NUMSTATEV,STATEV,NUMFIELDV,FIELDV,
     2 FIELDVINC,NUMPROPS,PROPS)
C
      INCLUDE 'ABA_PARAM.INC'
C
      CHARACTER*80 CMNAME
      DIMENSION U(2),UI1(3),UI2(6),UI3(6),STATEV(*),FIELDV(*),
     2 FIELDVINC(*),PROPS(*)
	 
	 
CC    FLAG FOR INCOMPRESSIBILITY
      INCMPFLAG=1.0D0 
      MU=PROPS(1)
      U(1)=BI1-3.0D0
      U(2)=0.0D0
      UI1(1)=MU/2.0D0
      UI1(2)=0.0D0
      UI1(3)=0.0D0
      UI2(1)=0.0D0
      UI2(2)=0.0D0
      UI2(3)=0.0D0
      UI2(4)=0.0D0
      UI2(5)=0.0D0
      UI2(6)=0.0D0
      UI3(1)=0.0D0
      UI3(2)=0.0D0
      UI3(3)=0.0D0
      UI3(4)=0.0D0
      UI3(5)=0.0D0
      UI3(6)=0.0D0 

      RETURN
      END