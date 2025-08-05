# Contributing to Home Automation System

We love your input! We want to make contributing to this home automation project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Pull Request Process

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Any contributions you make will be under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using Github's [issue tracker](https://github.com/yourusername/home_automation/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/yourusername/home_automation/issues/new).

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Feature Requests

We're always looking for suggestions to improve our home automation system. If you have an idea for a new feature:

1. Check if it's already been suggested in [issues](https://github.com/yourusername/home_automation/issues)
2. If not, create a new issue with the "enhancement" label
3. Describe the feature and why it would be useful
4. If possible, provide mockups or examples

## Code Style

### Flutter/Dart Code:
- Follow [Dart style guide](https://dart.dev/guides/language/effective-dart/style)
- Use `flutter format .` before committing
- Run `flutter analyze` to check for issues

### Python Code (ESP32):
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Keep functions small and focused
- Add comments for hardware-specific code

### Documentation:
- Use clear, concise language
- Include code examples where helpful
- Update README.md if adding new features

## Testing

### Flutter App:
- Write widget tests for new UI components
- Add integration tests for critical user flows
- Run `flutter test` before submitting PRs

### ESP32 Code:
- Test on actual hardware when possible
- Document any hardware requirements
- Include safety considerations in comments

## Development Setup

1. **Flutter Development:**
   ```bash
   flutter doctor
   flutter pub get
   flutter run
   ```

2. **ESP32 Development:**
   - Install MicroPython
   - Use Thonny IDE or similar
   - Test on breadboard before production

## Areas for Contribution

We especially welcome contributions in these areas:

### High Priority:
- Security improvements (authentication, encryption)
- Error handling and recovery
- Unit and integration tests
- Performance optimizations

### Medium Priority:
- New device types (sensors, cameras)
- UI/UX improvements
- Documentation improvements
- Code refactoring

### Low Priority:
- New platforms (web, desktop)
- Advanced features (scheduling, automation rules)
- Internationalization

## Getting Help

- Check existing [issues](https://github.com/yourusername/home_automation/issues)
- Read the [documentation](README.md)
- Join discussions in the issues section

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Code of Conduct

### Our Pledge

We are committed to making participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

---

Thank you for contributing to our home automation project! 🏡✨
