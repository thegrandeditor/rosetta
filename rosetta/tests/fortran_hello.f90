PROGRAM HELLO
    PRINT *, 'Hello, World!'
    CALL GREET('Rosetta')
END PROGRAM HELLO

SUBROUTINE GREET(NAME)
    CHARACTER(LEN=*) :: NAME
    PRINT *, 'Greetings, ', NAME
    IF (NAME == 'Rosetta') THEN
        PRINT *, 'You are the universal transpiler.'
    ELSE
        PRINT *, 'I do not know you.'
    END IF
END SUBROUTINE GREET
