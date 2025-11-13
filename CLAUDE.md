# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 중요: 언어 설정

**모든 대화는 한글로 진행합니다.** Claude Code와의 모든 상호작용, 설명, 응답은 반드시 한글로 작성해야 합니다.

## 프로젝트 개요

10개의 개별 웹 애플리케이션을 생성하고 하나의 index.html 파일로 연결하는 프롬프트 엔지니어링 실습 프로젝트입니다. AI 기반 개발을 위한 효과적인 프롬프트 작성 기법을 연습합니다.

## Technical Stack Constraints

- **HTML**: Single-file HTML documents for each feature
- **CSS**: Inline or embedded styles only (no external stylesheets)
- **JavaScript**: Vanilla JS only (no frameworks or libraries)
- **Python**: For backend features requiring server-side processing
- **Architecture**: All applications must be accessible from index.html via links

## Project Structure

```
/
├── index.html              # Main navigation page linking all 10 projects
├── project01/             # Individual project folders
│   ├── index.html
│   └── (optional .py files)
├── project02/
├── ...
├── project10/
├── prompts/               # Text files containing prompts used
│   ├── project01_prompt.txt
│   └── ...
├── screenshots/           # Execution result screenshots
│   ├── project01.png
│   └── ...
└── README.md             # Execution guide
```

## Prompt Engineering Standards

When creating prompts for this project, follow this structure:

### Required Prompt Components

1. **기능 (Functionality)**: Detailed description of what the feature does
2. **입력 (Input)**: Input format with concrete examples
3. **출력 (Output)**: Expected output format with examples
4. **예외처리 (Exception Handling)**: All edge cases and error scenarios to handle
5. **추가사항 (Additional Requirements)**: Code style, comments, accessibility

### Prompt Template

```
기능: [구체적인 기능 설명 - 사용자가 무엇을 할 수 있는지]

입력:
- 형식: [입력 데이터 타입]
- 예시: [구체적인 예시 3개 이상]
- 제약사항: [입력값의 범위, 형식 제한]

출력:
- 형식: [출력 데이터 타입 및 표시 방법]
- 예시: [예상되는 출력 결과]
- UI 요구사항: [사용자에게 보여지는 방식]

예외처리:
- 빈 입력값 처리
- 잘못된 형식 입력 처리
- 범위 초과 값 처리
- 네트워크/파일 오류 처리 (해당시)
- 사용자에게 명확한 에러 메시지 표시

추가사항:
- 코드에 한글 주석 포함
- 변수명은 의미있는 영문 사용
- 함수는 단일 책임 원칙 준수
- 사용자 친화적인 UI/UX
- 반응형 디자인 (모바일 대응)
```

## Development Guidelines

### HTML Structure Requirements

Each project HTML file must include:
- Proper DOCTYPE and semantic HTML5 structure
- Meta tags for charset and viewport
- Descriptive title and header
- Clear instructions for users
- All CSS embedded in `<style>` tags
- All JavaScript embedded in `<script>` tags

### Error Handling Requirements

Every project must handle:
- Invalid user input with user-friendly messages in Korean
- Empty or null values
- Type mismatches
- Boundary conditions (min/max values)
- Runtime errors with try-catch blocks
- Display errors in the UI, not just console

### Code Quality Standards

- **Comments**: All functions and complex logic must have Korean comments
- **Variable naming**: Use clear, descriptive English names (camelCase)
- **Function design**: Single responsibility, max 30 lines per function
- **Validation**: Always validate user input before processing
- **Accessibility**: Include ARIA labels and keyboard navigation support

### Index.html Requirements

The main index.html must:
- List all 10 projects with descriptive titles
- Include brief description of each project
- Provide working links to each project folder
- Have clean, organized layout
- Include navigation back to index from each project

## Commands

### Running Python Projects

If a project includes Python backend:

```bash
# Run Python server
cd project0X
python -m http.server 8000
# or for Python scripts
python script.py
```

### Testing HTML Projects

```bash
# Serve any HTML project locally
cd project0X
python -m http.server 8000
# Then open http://localhost:8000 in browser
```

## Deliverable Checklist

For each of the 10 projects, ensure:

- [ ] Functional code that runs without errors
- [ ] Screenshot of working application (screenshots/ folder)
- [ ] Prompt text file (prompts/ folder)
- [ ] Error handling implemented
- [ ] Korean comments in code
- [ ] Link added to index.html
- [ ] User instructions included in the HTML

## Submission Requirements

Final submission must include:

1. **실행 결과 스크린샷**: PNG/JPG files in screenshots/ folder
2. **사용한 프롬프트**: .txt files in prompts/ folder
3. **README.md**: Execution guide with:
   - How to run each project
   - Brief description of each feature
   - Any dependencies or requirements
   - Known issues or limitations

## Evaluation Criteria

| 평가 항목 | 배점 | 평가 내용 |
|---------|------|----------|
| 프롬프트 명확성 | 30% | 요구사항을 명확하게 전달했는가 |
| 코드 품질 | 30% | 생성된 코드가 정상 동작하는가 |
| 예외 처리 | 20% | 에러 처리를 요청했는가 |
| 문서화 | 20% | 주석과 설명을 포함했는가 |

## Prompt Engineering Best Practices

### Do's
- Specify exact input/output formats with examples
- List all edge cases and error scenarios
- Request specific error messages in Korean
- Ask for code comments in Korean
- Specify UI/UX requirements clearly
- Request validation for all user inputs
- Ask for mobile-responsive design

### Don'ts
- Avoid vague descriptions like "make it nice"
- Don't assume default behavior - specify everything
- Don't forget to mention single-file constraint
- Don't omit error handling requirements
- Don't request external libraries or frameworks

## Example Project Workflow

1. Write detailed prompt following the template
2. Save prompt to prompts/projectXX_prompt.txt
3. Generate code using Claude Code
4. Test thoroughly and fix any issues
5. Take screenshot of working application
6. Add link to index.html
7. Update README.md with execution instructions

## Common Patterns

### Form Input Validation
```javascript
function validateInput(value) {
    if (!value || value.trim() === '') {
        showError('입력값을 입력해주세요');
        return false;
    }
    // Additional validation
    return true;
}
```

### Error Display
```javascript
function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}
```

### Try-Catch Pattern
```javascript
try {
    // Main logic
    const result = processData(input);
    displayResult(result);
} catch (error) {
    showError('처리 중 오류가 발생했습니다: ' + error.message);
    console.error(error);
}
```

## Notes

- Each project should be self-contained and independent
- Focus on creating clear, educational examples
- Prioritize code readability over cleverness
- Test in multiple browsers (Chrome, Firefox, Safari)
- Ensure all Korean text displays correctly (UTF-8 encoding)
