      SUBROUTINE UANISOHYPER_INV (AINV, UA, ZETA, NFIBERS, NINV,
     1     UI1, UI2, UI3, TEMP, NOEL, CMNAME, INCMPFLAG, IHYBFLAG,
     2     NUMSTATEV, STATEV, NUMFIELDV, FIELDV, FIELDVINC,
     3     NUMPROPS, PROPS)
C
	     INCLUDE 'ABA_PARAM.INC' 
C
      CHARACTER*80 CMNAME
      DIMENSION AINV(NINV), UA(2), 
     2     ZETA(NFIBERS*(NFIBERS-1)/2)), UI1(NINV),
     3     UI2(NINV*(NINV+1)/2), UI3(NINV*(NINV+1)/2),
     4     STATEV(NUMSTATEV), FIELDV(NUMFIELDV),
     5     FIELDVINC(NUMFIELDV), PROPS(NUMPROPS)


      MU1=PROPS(1)
	  MU2=PROPS(2)
	  
	  BI1=AINV(1)
	  BI4=AINV(4)
      UA(1)=0.50D0*MU1*(BI1-3.0D0)+0.50D0*MU2*(BI4-1.0D0)**(2.0D0)
	  UI1(1)=0.50D0*MU1
	  UI1(2)=0.0D0
	  UI1(3)=0.0D0
	  UI1(4)=MU2*(BI4-1.0D0)
	  UI1(5)=0.0D0
	  UI1(6)=0.0D0
	  UI1(7)=0.0D0
	  UI1(8)=0.0D0
	  UI1(9)=0.0D0
	  UI2(10)=MU2
      RETURN
      END