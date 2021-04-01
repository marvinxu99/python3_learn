/* Query MEOWS Total RED */
SELECT distinct
;               D_TASK_ASSAY_DISP = UAR_GET_CODE_DISPLAY(D.TASK_ASSAY_CD)

               AVPU_SCORE = N.SHORT_STRING
               , RR_SCORE = N2.SHORT_STRING
               , SpO2_SCORE = N3.SHORT_STRING
               , O2_SCORE = N4.SHORT_STRING
               , SBP_SCORE = N5.SHORT_STRING
               , DBP_SCORE = N6.SHORT_STRING
               , HR_SCORE = N7.SHORT_STRING
               , TEMP_SCORE = N8.SHORT_STRING
               , TOTAL_RED = N81.SHORT_STRING

FROM
               DCP_INTERP   D

               , DCP_INTERP_STATE   DIS
               , NOMENCLATURE   N
;              , NOMENCLATURE   N11

               , DCP_INTERP_STATE   DIS2
               , NOMENCLATURE   N2
;              , NOMENCLATURE   N21


               , DCP_INTERP_STATE   DIS3
               , NOMENCLATURE   N3
;              , NOMENCLATURE   N31


               , DCP_INTERP_STATE   DIS4
               , NOMENCLATURE   N4
;              , NOMENCLATURE   N41

               , DCP_INTERP_STATE   DIS5
               , NOMENCLATURE   N5
;              , NOMENCLATURE   N51

               , DCP_INTERP_STATE   DIS6
               , NOMENCLATURE   N6
;              , NOMENCLATURE   N61

               , DCP_INTERP_STATE   DIS7
               , NOMENCLATURE   N7
;              , NOMENCLATURE   N71

               , DCP_INTERP_STATE   DIS8
               , NOMENCLATURE   N8
               , NOMENCLATURE   N81


PLAN D
where d.task_assay_cd = ( SELECT CV1.CODE_VALUE FROM CODE_VALUE CV1 
                                             WHERE cv1.display_key like "MEOWSTOTALRED" and cv1.code_set = 14003 )

JOIN DIS
where dis.dcp_interp_id = d.dcp_interp_id
and dis.input_assay_cd = (select di.component_assay_cd from DCP_INTERP_COMPONENT   DI
                                             where di.dcp_interp_id = d.dcp_interp_id and di.component_sequence = 1)
JOIN N
where n.nomenclature_id = dis.nomenclature_id
;and N.short_string = "Normal"                              /* Normal or Red */
;and N.short_string = "Red"                                     /* Normal or Red */
;JOIN N11
;where n11.nomenclature_id = dis.result_nomenclature_id                                           

                                             
JOIN DIS2
where dis2.dcp_interp_id = d.dcp_interp_id
               and dis2.input_assay_cd = (select di.component_assay_cd from DCP_INTERP_COMPONENT   DI
                                             where di.dcp_interp_id = d.dcp_interp_id and di.component_sequence = 2)
               and dis2.state = dis.resulting_state
JOIN N2
where n2.nomenclature_id = dis2.nomenclature_id                                          
;JOIN N21
;where n21.nomenclature_id = dis2.result_nomenclature_id                                         

                                             
JOIN DIS3
where dis3.dcp_interp_id = d.dcp_interp_id
               and dis3.input_assay_cd = (select di.component_assay_cd from DCP_INTERP_COMPONENT   DI
                                             where di.dcp_interp_id = d.dcp_interp_id and di.component_sequence = 3)
               and dis3.state = dis2.resulting_state
JOIN N3
where n3.nomenclature_id = dis3.nomenclature_id                                          
;JOIN N31
;where n31.nomenclature_id = dis3.result_nomenclature_id                                         
                                             
                                             
JOIN DIS4
where dis4.dcp_interp_id = d.dcp_interp_id
               and dis4.input_assay_cd = (select di.component_assay_cd from DCP_INTERP_COMPONENT   DI
                                             where di.dcp_interp_id = d.dcp_interp_id and di.component_sequence = 4)
               and dis4.state = dis3.resulting_state
JOIN N4
where n4.nomenclature_id = dis4.nomenclature_id                                          
;JOIN N41
;where n41.nomenclature_id = dis4.result_nomenclature_id                                         

                                             
JOIN DIS5
where dis5.dcp_interp_id = d.dcp_interp_id
               and dis5.input_assay_cd = (select di.component_assay_cd from DCP_INTERP_COMPONENT   DI
                                             where di.dcp_interp_id = d.dcp_interp_id and di.component_sequence = 5)
               and dis5.state = dis4.resulting_state
JOIN N5
where n5.nomenclature_id = dis5.nomenclature_id                                          
;JOIN N51
;where n51.nomenclature_id = dis5.result_nomenclature_id                                         

                                             
JOIN DIS6
where dis6.dcp_interp_id = d.dcp_interp_id
               and dis6.input_assay_cd = (select di.component_assay_cd from DCP_INTERP_COMPONENT   DI
                                             where di.dcp_interp_id = d.dcp_interp_id and di.component_sequence = 6)
               and dis6.state = dis5.resulting_state
JOIN N6
where n6.nomenclature_id = dis6.nomenclature_id                                          
;JOIN N61
;where n61.nomenclature_id = dis6.result_nomenclature_id                                         

                                             
JOIN DIS7
where dis7.dcp_interp_id = d.dcp_interp_id
               and dis7.input_assay_cd = (select di.component_assay_cd from DCP_INTERP_COMPONENT   DI
                                             where di.dcp_interp_id = d.dcp_interp_id and di.component_sequence = 7)
               and dis7.state = dis6.resulting_state
JOIN N7
where n7.nomenclature_id = dis7.nomenclature_id                                          
;JOIN N71
;where n71.nomenclature_id = dis7.result_nomenclature_id                                         

                                             
JOIN DIS8
where dis8.dcp_interp_id = d.dcp_interp_id
               and dis8.input_assay_cd = (select di.component_assay_cd from DCP_INTERP_COMPONENT   DI
                                             where di.dcp_interp_id = d.dcp_interp_id and di.component_sequence = 8)
               and dis8.state = dis7.resulting_state
JOIN N8
where n8.nomenclature_id = dis8.nomenclature_id                                          
JOIN N81
where n81.nomenclature_id = dis8.result_nomenclature_id                           

ORDER by 
               AVPU_SCORE
               , RR_SCORE
               , SPO2_SCORE
               , O2_SCORE
               , SBP_SCORE
               , DBP_SCORE
               , HR_SCORE
               , TEMP_SCORE 

WITH maxrecrec=60000, time=60




/* Query total rows for MEOWS TOTAL RED */
SELECT
	DI_COMPONENT_ASSAY_DISP = UAR_GET_CODE_DISPLAY(DI.COMPONENT_ASSAY_CD)
	, count(*)

FROM
	DCP_INTERP   D
	, DCP_INTERP_COMPONENT   DI
	, DCP_INTERP_STATE   DIS

PLAN D
where d.task_assay_cd = ( SELECT CV1.CODE_VALUE FROM CODE_VALUE CV1 
                                             WHERE cv1.display_key ="MEOWSTOTALRED" and cv1.code_set = 14003 )


                                             
JOIN DI
where d.dcp_interp_id = di.dcp_interp_id
;and di.component_sequence = 1     
;and di.component_sequence = 2
;and di.component_sequence = 3
;and di.component_sequence = 4
;and di.component_sequence = 5
;and di.component_sequence = 6
;and di.component_sequence = 7
;and di.component_sequence = 8

JOIN DIS
where dis.dcp_interp_id = d.dcp_interp_id
and dis.input_assay_cd = di.component_assay_cd

GROUP BY
	DI.COMPONENT_ASSAY_CD


WITH MAXREC = 10000



/* Query total rows for MEOWS TOTAL RED */
SELECT
               count(dis.dcp_interp_id)
FROM
               DCP_INTERP   D
               , DCP_INTERP_COMPONENT   DI
               , DCP_INTERP_STATE   DIS

where d.task_assay_cd = ( SELECT CV1.CODE_VALUE FROM CODE_VALUE CV1 
                                             WHERE cv1.display_key ="MEOWSTOTALRED" and cv1.code_set = 14003 )
                                             
               and d.dcp_interp_id = di.dcp_interp_id
               and dis.dcp_interp_id = d.dcp_interp_id
               and dis.updt_cnt >= 0

WITH MAXREC = 10000



SELECT
               D_TASK_ASSAY_DISP = UAR_GET_CODE_DISPLAY(D.TASK_ASSAY_CD)
;              , D.AGE_FROM_MINUTES
;              , D.AGE_TO_MINUTES
               , DI_COMPONENT_ASSAY_DISP = UAR_GET_CODE_DISPLAY(DI.COMPONENT_ASSAY_CD)
               , DI.COMPONENT_SEQUENCE
;              , DI.DESCRIPTION
               , DI.LOOK_AHEAD_MINUTES
               , DI.LOOK_BACK_MINUTES
               , DIS_INPUT_ASSAY_DISP = UAR_GET_CODE_DISPLAY(DIS.INPUT_ASSAY_CD)
;              , DIS.NOMENCLATURE_ID
               , DIS.NUMERIC_LOW
               , DIS.NUMERIC_HIGH
               , N.SHORT_STRING
               , DIS.RESULTING_STATE
;              , DIS.RESULT_NOMENCLATURE_ID
               , DIS.STATE
               , N2.SHORT_STRING
               , DIS.RESULT_VALUE

FROM
               DCP_INTERP   D
               , DCP_INTERP_COMPONENT   DI
               , DCP_INTERP_STATE   DIS
               , NOMENCLATURE   N
               , NOMENCLATURE   N2

where d.task_assay_cd = ( SELECT CV1.CODE_VALUE FROM CODE_VALUE CV1 
;                                            WHERE cv1.display_key like "MEOWS*SCORE" and cv1.code_set = 14003 )
                                             WHERE cv1.display_key like "MEOWSUNU*" and cv1.code_set = 14003 )
                                             
               and d.dcp_interp_id = di.dcp_interp_id
               and dis.dcp_interp_id = d.dcp_interp_id
               and dis.nomenclature_id = n.nomenclature_id
               and dis.result_nomenclature_id = n2.nomenclature_id

WITH MAXREC = 20000


/* Query MEOWS Total RED */
SELECT distinct
               D_TASK_ASSAY_DISP = UAR_GET_CODE_DISPLAY(D.TASK_ASSAY_CD)
               , d.dcp_interp_id
;              , D.AGE_FROM_MINUTES
;              , D.AGE_TO_MINUTES
               , DI_COMPONENT_ASSAY_DISP = UAR_GET_CODE_DISPLAY(DI.COMPONENT_ASSAY_CD)
               , DI.COMPONENT_SEQUENCE
;              , DI.DESCRIPTION
               , DI.LOOK_AHEAD_MINUTES
               , DI.LOOK_BACK_MINUTES
               , DIS_INPUT_ASSAY_DISP = UAR_GET_CODE_DISPLAY(DIS.INPUT_ASSAY_CD)
;              , DIS.NOMENCLATURE_ID
;              , DIS.NUMERIC_LOW
;              , DIS.NUMERIC_HIGH
               , N.SHORT_STRING
               , DIS.RESULTING_STATE
;              , DIS.RESULT_NOMENCLATURE_ID
               , DIS.STATE
               , N2.SHORT_STRING
               , DIS.RESULT_VALUE

FROM
               DCP_INTERP   D
               , DCP_INTERP_COMPONENT   DI
               , DCP_INTERP_STATE   DIS
               , NOMENCLATURE   N
               , NOMENCLATURE   N2

where d.task_assay_cd = ( SELECT CV1.CODE_VALUE FROM CODE_VALUE CV1 
                                             WHERE cv1.display_key like "MEOWSTOTALRED" and cv1.code_set = 14003 )
                                             
               and d.dcp_interp_id = di.dcp_interp_id
               and dis.dcp_interp_id = d.dcp_interp_id
               and dis.nomenclature_id = n.nomenclature_id
               and dis.result_nomenclature_id = n2.nomenclature_id

WITH MAXREC = 200000



