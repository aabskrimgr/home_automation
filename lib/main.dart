import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(const HomeAutomationApp());
}

class HomeAutomationApp extends StatelessWidget {
  const HomeAutomationApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Home Automation',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final DatabaseReference _database = FirebaseDatabase.instance.ref('led_state');

  Map<String, bool> buttonStates = {
    'room1': false,
    'room2': false,
    'room3': false,
    'freeze': false,
    'ac': false,
    'main': false,
  };

  @override
  void initState() {
    super.initState();
    _loadStatesFromFirebase();
  }

  Future<void> _loadStatesFromFirebase() async {
    final snapshot = await _database.get();
    if (snapshot.exists) {
      final data = Map<String, dynamic>.from(snapshot.value as Map);
      setState(() {
        data.forEach((key, value) {
          buttonStates[key] = value == 1;
        });
      });
    }
  }

  void _toggleState(String key) {
    final newState = !buttonStates[key]!;
    setState(() {
      buttonStates[key] = newState;
    });
    _database.child(key).set(newState ? 1 : 0);
  }

  Widget _buildButton(String label) {
    final isActive = buttonStates[label] ?? false;
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6.0),
      child: ElevatedButton(
        onPressed: () => _toggleState(label),
        style: ElevatedButton.styleFrom(
          backgroundColor: isActive ? Colors.green : Colors.grey,
          padding: const EdgeInsets.symmetric(vertical: 18),
          textStyle: const TextStyle(fontSize: 18),
        ),
        child: Text(
          '${label.toUpperCase()}: ${isActive ? "ON" : "OFF"}',
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home Automation'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: ListView(
          children: [
            _buildButton('room1'),
            _buildButton('room2'),
            _buildButton('room3'),
            const Divider(),
            _buildButton('freeze'),
            _buildButton('ac'),
            _buildButton('main'),
          ],
        ),
      ),
    );
  }
}
