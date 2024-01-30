# PISA Practice Platform

This project integrates a computational program designed to enhance the skills and knowledge of 15-year-old students in the three focus areas assessed by the PISA test: reading, mathematics, and science.

**Final Integrative Project**  
**Educational Unit:** TC1028 - Computational Thinking for Engineering  
**Student:** Emmanuel Naranjo - A00835705

## Usage:
1. Run the script (`main.py`).
2. Choose options to register, practice, view summaries, or exit.
3. Progress is saved, and students can track their performance.

## Code (`main.py`)
The Python script (`main.py`) comprises a set of functions that facilitate students' practice in the key subjects evaluated by the PISA test. It provides quizzes in mathematics, Spanish, and science, along with functionalities such as student registration, progress tracking, and session summaries.

### Functions:
1. **`revision(respuestas, resultado)`**
   - Checks the user's answers against correct quiz answers.
   - Returns a score based on 100 points.

2. **`guardar(nombre, calificacion_M, calificacion_E, calificacion_C)`**
   - Saves the student's progress in a text file.
   - Records the practices performed in each attempt.

3. **`resumen(nombre)`**
   - Displays a summary of the student's progress, attempts, and scores by topic.

4. **`estudiantes(lista_estudiantes)`**
   - Lists all students currently practicing on the platform.

5. **`pruebaMate()`**
   - Evaluates the student's performance in mathematics with a quiz.

6. **`pruebaEspanhol()`**
   - Evaluates the student's performance in Spanish with a quiz.

7. **`pruebaCiencias()`**
   - Evaluates the student's performance in science with a quiz.

#### File Handling:
- The code searches for and manages student files in the current directory (`lista_estudiantes`).

### Main Menu:
- **Option 'a':** Student Registration.
- **Option 'b':** Practice Topics:
  - Mathematics
  - Spanish
  - Science
  - Save and Exit
- **Option 'c':** Display Students Currently Practicing.
- **Option 'd':** View Student Summary.
- **Option 'e':** Exit the Program.
