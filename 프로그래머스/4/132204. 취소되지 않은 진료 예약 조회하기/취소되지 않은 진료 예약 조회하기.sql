
SELECT 
    A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM 
    PATIENT AS P 
    JOIN
        DOCTOR AS D 
    JOIN
        (
            SELECT APNT_YMD, APNT_NO, PT_NO, MDDR_ID
            FROM APPOINTMENT
            WHERE DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
                AND APNT_CNCL_YN = 'N'
                AND MCDP_CD = 'CS'
        ) AS A
    ON 
        P.PT_NO = A.PT_NO AND D.DR_ID = A.MDDR_ID
ORDER BY
    A.APNT_YMD;

