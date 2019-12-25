package singleton

import "sync"

// Singleton .
type Singleton struct {
	Name string
}

var singleInstance *Singleton
var once sync.Once

// GetSingleInstance .
func GetSingleInstance() *Singleton {
	once.Do(func() {
		singleInstance = &Singleton{}
	})
	return singleInstance
}

// SetName .
func (s *Singleton) SetName(name string) {
	s.Name = name
}
