package singleton

import (
	"fmt"
	"testing"
	"sync"
	"strconv"
)


func TestGetInstance(t *testing.T) {
	for i := 0; i < 5; i++ {
		object := GetSingleInstance()
		object.SetName("name" + strconv.Itoa(i))
		fmt.Printf("%p %+v\n", object, *object)	
	}

	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go 	func( ){
			object := GetSingleInstance()
			fmt.Printf("%p %+v\n", object, *object)	
			wg.Done()
		}()
	}
	wg.Wait()
}
